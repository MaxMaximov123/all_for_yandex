import requests
from tqdm import tqdm
import json
from pprint import pprint
from threading import Thread
import os


class Lessons:
    def __init__(self, cookie, path, group_id, course_id):
        self.group_id = group_id
        self.head = {
            'cookie': cookie}

        self.path = path
        self.data = {}
        self.data1 = {}

        r = requests.get(f'https://lyceum.yandex.ru/api/student/tasks?courseId={course_id}&groupId={self.group_id}&limit=999999',
                         headers=self.head)
        results = json.loads(r.content)['results']
        list1 = []
        list2 = []
        olo = []
        for i in tqdm(results):
            list1.append(i['id'])
            # b = Thread(target=self.a, args=(i['id'],))
            # b.start()
            # olo.append(b)

        # [i.join() for i in olo]
        # pprint(sorted(list1))
        for i in tqdm(range(25600, 30000)):
            if i not in list1:
                b = Thread(target=self.a, args=(i,))
                b.start()
                olo.append(b)
        [i.join(timeout=1) for i in tqdm(olo)]
        # b.join()
        print(999)
        with open('new_data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data1, f, ensure_ascii=False, indent=4)
        # print(self.data1)
        # print('start_of saving')
        # self.save_data(self.data)
        print('ok')

    def a(self, i):
        try:
            r = requests.get(f"https://lyceum.yandex.ru/api/student/tasks/{i}?groupId={self.group_id}", headers=self.head)
            if r.status_code == 200:
                r = json.loads(r.content)
                local_data = self.data1.get(r['lesson']['title'], {})
                local_data.update({'title': r})
                self.data1[r['lesson']['title']] = local_data
                # pprint(r)
                # titles = self.data.get(r['lesson']['title'], {})
                # titles.update({r['title']: r['latestSubmission']['file']['url']})
                # self.data[r['lesson']['title']] = titles
        except Exception as e:
            pass
            # print(999)
            # print(e)

    def save(self, url, path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)

    def replacee(self, text):
        for i in ':;!@#$%^&*/\{]}[<>?|"':
            text = text.replace(i, '')
        return text

    def save_data(self, json1):
        for i in tqdm(json1):
            newpath = f'{self.path}{self.replacee(i)}'
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            for j in json1[i]:
                t = Thread(target=self.save, args=(json1[i][j], f'{self.path}{self.replacee(i)}/{self.replacee(j)}.py'))
                t.start()


cookie2 = 'gdpr=0; mda=0; yandexuid=8132644331649949022; yuidss=8132644331649949022; ymex=1965312843.yrts.1649952843; amcuid=92652121654611035; is_gdpr=0; is_gdpr_b=COiIMxDZgwEoAg==; L=cVp1VWoBZ2JzbXxGRmFTTg9/CQ5HY1hWWyQwIxFELGQD.1661928096.15086.397812.bfb6bf4212c7786204f9789ae080b968; yandex_login=maxss.k2n; mda2_domains=kinopoisk.ru; i=MFsTcHEhEWY7c8K3ymcDYlJZ/5HvGuI9GAkxL0kMe38MJHDksdIDAsqS9sYHYE8gMFVCqOPQd/gEGM8ZwvCG5aiGCzo=; yabs-frequency=/5/2W060FgpXsFP8o9Z/; Session_id=3:1669910207.5.0.1660583623972:3_nMsg:44.1.1:czoxNjQ5OTQ5MDc4MTU1OkI3c1gyUTo0.2:1|883187617.-1.2|3:10261977.459792.U3MvvYGdJEQHp0nlk9ukUrU3d0I; sessionid2=3:1669910207.5.0.1660583623972:3_nMsg:44.1.1:czoxNjQ5OTQ5MDc4MTU1OkI3c1gyUTo0.2:1|883187617.-1.2|3:10261977.459792.fakesign0000000000000000000; sae=0:EA62411B-0F8D-4F32-A299-9008CE08666F:p:22.11.0.2500:w:d:RU:20210226; csrftoken=uedd9f1b7c60eeedc18ceea4a01e412dd; gdpr=0; instruction=1; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1670010734715227-11956845481056020862-vla1-0276-vla-l7-balancer-8080-BAL-989#ybzcc.ru#newsca.native_cache; _yasc=6Sb3eDO4MOZVFeiAzI+jMQ1v10t/4BK89xR5VNFfS5RIvcqJLkxwdaSOiVe8tilO; yp=1670078768.uc.ru#1670078768.duc.ru#1684563272.szm.1:1920x1080:1920x940#1699622629.cld.2261448#1699622629.brd.0699000022#1701529362.pgp.4_27833222#1671622050.csc.1#1670018766.gpauto.55_758255:49_237934:140:1:1670011566#1670598162.mcv.6#1670598162.mcl.1695r7s'
cookie1 = 'ys=newsca.native_cache#ybzcc.ru#svt.1#def_bro.1#ead.2FECB7CF; yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; my=YwA=; _ym_d=1657999835; skid=5722487791658000552; is_gdpr=0; is_gdpr_b=CPDcKRCxhQEoAg==; i=GLuIMg84/KWSdhu1Ca1cilvcoNOETGLu6Z0p1jcnZIWFbMtt1epf9pYtYDOjHzuHTX1oEStxcihjndBNwGeSYkKAEv4=; Session_id=3:1669888412.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10261965.901766.rTfeLAT8m6aFoQLlbiG8pzHpjPU; sessionid2=3:1669888412.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10261965.901766.fakesign0000000000000000000; _ym_isad=2; yabs-frequency=/5/3m0f04EKYsFJw2PZ/IkQnfDqwfKQOIIu0/; csrftoken=ub6cc65f2be5813b518d8a2afc97f64b8; instruction=1; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.11.0.2500:w:d:RU:20211231; _yasc=/MLwAGZU2AaXPkKrSvHGHvLW/rOnAJpmd4I9aNHwbRpu+i/uwxe8MEVeYkniehdCdHG3Am5DSIhHP6izcDzosbyh; yp=1670187842.uc.ru#1670187842.duc.ru#1681416026.cld.2261448#1681416026.brd.0699000036#1979804395.skin.l#1980767386.pcs.1#1979804396.dark_promo.5#1699813142.pgp.5_27804612#1684801537.szm.1_375:1536x864:1353x660#1671712136.csc.1#1670258490.mcv.6#1670258490.mcl.1695r7s#1670111042.gpauto.55_877686:49_746178:140:1:1670103842; _ym_visorc=w'
cookie3 = 'ys=newsca.native_cache#ybzcc.ru#svt.1#def_bro.1#ead.2FECB7CF; yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; my=YwA=; _ym_d=1657999835; skid=5722487791658000552; is_gdpr=0; is_gdpr_b=CPDcKRCxhQEoAg==; i=GLuIMg84/KWSdhu1Ca1cilvcoNOETGLu6Z0p1jcnZIWFbMtt1epf9pYtYDOjHzuHTX1oEStxcihjndBNwGeSYkKAEv4=; Session_id=3:1669888412.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10261965.901766.rTfeLAT8m6aFoQLlbiG8pzHpjPU; sessionid2=3:1669888412.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10261965.901766.fakesign0000000000000000000; _ym_isad=2; yabs-frequency=/5/3m0f04EKYsFJw2PZ/IkQnfDqwfKQOIIu0/; instruction=1; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.11.0.2500:w:d:RU:20211231; csrftoken=ufd6173ee47d99ce6065ab0daf3f388a5; yp=1670223544.uc.ru#1670223544.duc.ru#1681416026.cld.2261448#1681416026.brd.0699000036#1979804395.skin.l#1980767386.pcs.1#1979804396.dark_promo.5#1699813142.pgp.5_27804612#1684801537.szm.1_375:1536x864:1353x660#1671712136.csc.1#1670258490.mcv.6#1670258490.mcl.1695r7s#1670149744.gpauto.55_877686:49_746178:140:1:1670142544; _yasc=6Ix0+KzJK+ZPTBBKwrE8SrJKl9DUexG5l2iu9YuTbhSDMm/Mxs3IcXpWrbUlN1seXWzRgKrD8rZYZXX16Bgp9Cof'
l = Lessons(cookie3, 'C:/yandex_lessons/2 Курс/', 6393, 766)