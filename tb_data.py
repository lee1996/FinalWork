import requests
from bs4 import BeautifulSoup
import re
tb_url1='https://item.taobao.com/item.htm?spm=a230r.1.14.303.7ec015a8y5LCZO&id=563702123181&ns=1&abbucket=17#detail'
tb_com_url1='https://rate.taobao.com/feedRateList.htm?auctionNumId=563702123181&userNumId=1938000557&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hvb9vEvbQvjQCkvvvvvjiPPLdZtjiUPLzpQj3mPmPO1ji8PssvsjEhn2zOljItvpvhvvvvvbyCvm9vvvvWphvvvvvvvwivpv9ivvmm86Cv2vvvvUUdphvUi9vv9krvpvkeuphvmvvv9bCfKI6AkphvC99vvpH0BpyCvhQWEQZvC0eviNoxdX368Nswtnv4jcH26WLh%2B2Kz8Z0vQRAn%2BbyDCwFhTWeARFxjKOmxfXKKNB3rlj7Q%2BulAbMoxfwkKDox%2Fzj7QD40fvphvC9vhvvCvpvGCvvpvvPMMiQhvCvvv9U8jvpvhvvpvvv%3D%3D&_ksTS=1516591211702_1549&callback=jsonp_tbcrate_reviews_list'
tb_url2='https://item.taobao.com/item.htm?id=556946894428&ali_trackid=2:mm_26632614_0_0:1516584234_318_536331383&spm=a21bo.7925826.192013.3.1ea742c5j0YHZS'
tb_com_url2='https://rate.taobao.com/feedRateList.htm?auctionNumId=556946894428&userNumId=2130851634&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hvTQvEvbQvUvCkvvvvvjiPPLdZgjYbn2FU1jnEPmPvsjnVR2LpljlhPFShzj3CRphvCvvvvvvPvpvhvv2MMqyCvm9vvvvWphvvvvvvvJ3vpv9ivvmm86Cv2vvvvUUdphvUi9vv9krvpvkeuphvmvvv9bCfUNfrkphvC99vvpH0BpyCvhQh6uhvC0kDyO2vHdUfbjc6D70XdeQHYExrz8TNahNU6RF9VXDscYeYiXhpVj%2BO3w0x9Ek4J9kx6acEn1viHExr1WoK5zEClWsI1EA4vphvC9vhvvCvp8wCvvpvvUmm3QhvCvvhvvv%3D&_ksTS=1516584484361_1619&callback=jsonp_tbcrate_reviews_list'
headers = {
    'Cookie': 'cna=2L+FEQUj4hcCAbfAXdikda8c; l=AtnZ9oiWaPSjUUftl30cvcXqac6zxc1b; t=761823bfa80836d34300d5992df1c3b0; thw=cn; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _cc_=WqG3DMC9EA%3D%3D; lgc=leet96; tracknick=leet96; ucn=center; enc=goEeFtR2bToJU1tGj3BOn4uqvnMWyI8UAcA3ubR73wdxpAJfOQ2E%2BSIjwtT%2FIdZQB58VU7HKPpIp1Qqoqf7Vog%3D%3D; uc3=sg2=WvX3PhtDHwnTB6szYiikdAsdGpLEkHN8mOCQDrn5GTo%3D&nk2=D8bhXnHd&id2=UNGXEr3fwoUreg%3D%3D&vt3=F8dBzLgqZ1fEl4mFESM%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTUxNTg5NjA0MQ%3D%3D; uss=WvKV6z8uDwVem1SG1vyqu2tN%2FIk8afcO06NODCrizyWQG7znouFjNfow; sg=689; mt=np=&ci=8_1; cookie1=B0f0IZxeVU68RpwAQ1blVfDWM1YN72shoSZABqnHbD0%3D; unb=3110883738; skt=40adb9c6e23919b8; _l_g_=Ug%3D%3D; _nk_=leet96; cookie17=UNGXEr3fwoUreg%3D%3D; uc1=cookie14=UoTdfkOYuU2m4A%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; isg=ArCw7_BinumkpkL_uDGGqbuCgXfCUZUzQl0YKKoBVYveZVAPUglk0wZVyVP5; v=0; cookie2=1e4b7783c9f5b8d26bb817cafc73e8ac; _tb_token_=e7d4be8b4e313',
    'User Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
    'Referer': 'https://item.taobao.com/item.htm?'
}

def crawler_tb(goods_url,comment_url):
    headers = {
        'Cookie': 'cna=2L+FEQUj4hcCAbfAXdikda8c; l=AtnZ9oiWaPSjUUftl30cvcXqac6zxc1b; t=761823bfa80836d34300d5992df1c3b0; thw=cn; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _cc_=WqG3DMC9EA%3D%3D; lgc=leet96; tracknick=leet96; ucn=center; enc=goEeFtR2bToJU1tGj3BOn4uqvnMWyI8UAcA3ubR73wdxpAJfOQ2E%2BSIjwtT%2FIdZQB58VU7HKPpIp1Qqoqf7Vog%3D%3D; uc3=sg2=WvX3PhtDHwnTB6szYiikdAsdGpLEkHN8mOCQDrn5GTo%3D&nk2=D8bhXnHd&id2=UNGXEr3fwoUreg%3D%3D&vt3=F8dBzLgqZ1fEl4mFESM%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTUxNTg5NjA0MQ%3D%3D; uss=WvKV6z8uDwVem1SG1vyqu2tN%2FIk8afcO06NODCrizyWQG7znouFjNfow; sg=689; mt=np=&ci=8_1; cookie1=B0f0IZxeVU68RpwAQ1blVfDWM1YN72shoSZABqnHbD0%3D; unb=3110883738; skt=40adb9c6e23919b8; _l_g_=Ug%3D%3D; _nk_=leet96; cookie17=UNGXEr3fwoUreg%3D%3D; uc1=cookie14=UoTdfkOYuU2m4A%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; isg=ArCw7_BinumkpkL_uDGGqbuCgXfCUZUzQl0YKKoBVYveZVAPUglk0wZVyVP5; v=0; cookie2=1e4b7783c9f5b8d26bb817cafc73e8ac; _tb_token_=e7d4be8b4e313',
        'User Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
        'Referer': 'https://item.taobao.com/item.htm?'
    }
    if re.findall('^https://rate.taobao.com/',comment_url):
        tb_data2=requests.get(url=comment_url,headers=headers)
        comment_content=BeautifulSoup(tb_data2.text,'lxml').text
        # print(comment_content)
        comment_all=[]
        comment = re.findall('("content":.*?),"rateId"', comment_content)
        for data in comment:
            if '"buyAmount"' in data:
                data = re.split('"content":', data)[3]
                comment_all.append(data[:-1])
            else:
                data = data[11:]
                comment_all.append(data[:-1])
        #print('真实价格为　%s' % real_price)
        # i=1
        # for com in comment_content_data:
        #     print('第 %d 条评论为　%s' % (i,com))
        #     i+=1
        #print('评论为　%s' % comment_content_data)
        totals=re.findall('("total":.*?),"comments"',comment_content)[0]
        total=int(re.findall('(\d+)',totals)[0])
        #print('总评论数为　%d '% total)
        # print('第1页的评论为%s '% comment_all)
        i=0
        for data in comment_all:
            i+=1
        # print('第一页的评论数为　%d' % i)
        if i==total:
            print('评论只有一页')
        else:
            for j in range(1,1000):
                comment_url = comment_url.replace('currentPageNum=%d'% j, 'currentPageNum=%d' % (j+1))
                tb_data2 = requests.get(url=comment_url, headers=headers)
                comment_content = BeautifulSoup(tb_data2.text, 'lxml').text
                comment_content_data = re.findall('("content":.*?),"rateId"', comment_content)
                u=0
                for data in comment_content_data:
                    if '"buyAmount"' in data:
                        data=re.split('"content":',data)[3]
                        comment_all.append(data[:-1])
                    else:
                        data = data[11:]
                        comment_all.append(data[:-1])
                    u+=1

                # print('第　%d 页的评论数为　%d' % (j+1,u))
                # print('第%d页的评论为%s' % (j + 1, comment_content_data))
                i=i+u
                if i==total:
                    break
                j+=1
        # print('所有的评论为　%s' %comment_all)
        request=requests.get(goods_url,headers=headers)
        soup=BeautifulSoup(request.text,'lxml')
        assurance=soup.select('#J_ShopInfo > div > div.tb-shop-info-hd > div.tb-shop-icon > dl > dd > a.tb-seller-bail > span.tb-seller-bail-text')[0]
        money=int(re.findall(r'(\d+)',str(assurance))[0])
        # print('保证金为　%d' %money)
        startTime=soup.select('#J_ShopInfo > div > div.tb-shop-info-hd > div.tb-shop-icon > dl > dd > a.tb-icon.tb-icon-alipay-persion-auth')[0]
        startTime=re.findall('(title=".*?")',str(startTime))[0][7:][:-1]
        # print('认证时间为　%s' % startTime)
        result={
            'comment':comment_all,
            'startTime':startTime,
            'comment_count':total,
            'assurance':money
        }
        return result

    else:
        print('无该商品')
        return None

result=crawler_tb(goods_url=tb_url1,comment_url=tb_com_url1)
if result:
    assurance=result['assurance']
    startTime=result['startTime']
    comment=result['comment']
    comment_count=result['comment_count']
else:
    print('fuck you no such goods')
print('总评论数为:　%d '% comment_count)
print('保证金为:　%d' % assurance)
print('认证时间为:　%s' % startTime)
i=0
for data in comment:
    if ('整体感觉' in data) or ('质量不错' in data) or (len(data)>100):
        i+=1
print('可能存在恶意刷评论的评论数为:　%d' % i)
print('所有评论如下:\n')
from pandas import DataFrame
import numpy as np

data=DataFrame(comment,columns=['评论'])
length=data.count()
# path='data/data.csv'
# print(data)
import matplotlib as mpl
import matplotlib.pyplot as plt


labels=['deliberate','other']
sizes=[i,length-i]
explode=(0.1,0)
plt.title('The Rate of TaoBao Comments of Deliberate ')
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()







