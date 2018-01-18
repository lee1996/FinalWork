import requests
from bs4 import BeautifulSoup
import re

tm_com_url='https://rate.tmall.com/list_detail_rate.htm?itemId=557114566133&spuId=868515218&sellerId=779984393&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hv8QvWvRyvUvCkvvvvvjiPPL5y1jnVP259AjYHPmPhzjDERFcWzjDPRF59Ajn8dphvmpvUhUhn2pv%2BBFyCvvpvvvvv9phvHHifsPwQzHi47eUMtMQb76t4snYUvphvC9vhvvCvpvyCvhQhfuOvCzVYiXVvVE6Fp%2B0x9WpOjLEc6acEKBm6NB3r1W1ljdUf8%2BBlKbVAnAaLINshQCAwJhbUlWFpHF%2BSBiVvQRA1%2B2n79WLhT2eAKphv8vvvvv1vpvvvvvvCi6CvmmyvvUUdphvWvvvv9krvpvkevvmm86Cvm84EvpvVmvvCvcXHuphvmvvv92msJYTH2QhvCvvvMMGtvpvhvvvvv8wCvvpvvUmm3QhvCvvhvvv%3D&isg=AnNzJuUKLUGlweEbxnWiwCb0An5dAAYaNby78SUQ-RLJJJLGrXkJuyu2qmo2&needFold=0&_ksTS=1515918510351_559&callback=jsonp560'
tm_pri_url='https://mdskip.taobao.com/core/initItemDetail.htm?household=false&addressLevel=2&isAreaSell=false&queryMemberRight=true&showShopProm=false&service3C=false&sellerPreview=false&offlineShop=false&cartEnable=true&isForbidBuyItem=false&tmallBuySupport=true&itemId=557114566133&isUseInventoryCenter=false&isSecKill=false&tryBeforeBuy=false&isApparel=true&isPurchaseMallPage=false&cachedTimestamp=1515916721998&isRegionLevel=false&callback=setMdskip&timestamp=1515918502560&isg=null&isg2=AsfHKrjaUQXxdtWHWtHOhPKYVnJRZJreASDvTZm2U9ZwCOfKoZwr_gWI3vaq&ref=https%3A%2F%2Fallin.tmall.com%2Fp%2Frd411227.htm%3Fspm%3Da1z10.1-b-s.w12037119-16894472638.9.2fd23c10Y0NU9f'
tb_pri_url='https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=563567576634&sellerId=2762091348&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess'
tb_com_url='https://rate.taobao.com/feedRateList.htm?auctionNumId=563567576634&userNumId=2762091348&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=106%23%2BYoBPQBkBtkB2BKaBBBBBpZb54Efo0Ky54%2FYy0Zc5W4Uo0ib5VRUk05s54YZy0%2BbLboBXlDv3eVSWG1oaboBKItv3Td1IXsKBXgi4gOGylmi4IDv3OrbyldD1Zz1Bcmb1OHi4gsmylmu%2FcDvlClbylvujCoK2u9qCl7hQQ%2BUKe1I7cvmouJ9nXoIc%2Bs5GY0FnWcuQYGwWmBsn84fKN%2Fn6P%2BRr%2FY980OxdAF%2FNiOapX2gdFaeCQCYC4CZHSQqvs%2FwdP3rPDpsCVdhtFakAA%2FnvN9Oc%2Bzm9KizG4hINpDYohtO6q68BP9AdVxISt%2B9nKdz2j4YuY0FARCR%2BqwGpVi%2B34ss1JEDtCZE2fHFuK1UoVtxnlIADmk5dXsTy%2BZn6Oxh5gl%2FOK2IKeK%2F%2B7gnou2o5UQqFxkA9sSjGXVRiC0aBuog%2BdvRfRyD3jLMwxy36B0inVucRDtTAedUt6w9WAxAduOia2DX9YTH2fwRhQ%2BPAR0Y5IvffRzX54ON1JLq8Y1wGXPEgfTBojys2Iv5oPt3dK1Urx1KtD0idxyKBmrhJvJ0lehEkxxpmNK4lJxpbXdTmSIAbfwECYCFYguGCyQEmVlnYSkram%2BVmgswaX3ntWGQcLq5t8zrSboBKIDq3pVbyBLKBBCBBG8plCoBKAJMQ2oIBCBo7NFKO6oKBB7i4RO0yntJBCBD1Zwz0Orb1ZHi4jGDkkni5I0b34L1BCBo7NFBQC%3D%3D&_ksTS=1515915914555_1232&callback=jsonp_tbcrate_reviews_list'
headers = {
    'Cookie': 'cna=2L+FEQUj4hcCAbfAXdikda8c; l=AtnZ9oiWaPSjUUftl30cvcXqac6zxc1b; t=761823bfa80836d34300d5992df1c3b0; thw=cn; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _cc_=WqG3DMC9EA%3D%3D; lgc=leet96; tracknick=leet96; ucn=center; enc=goEeFtR2bToJU1tGj3BOn4uqvnMWyI8UAcA3ubR73wdxpAJfOQ2E%2BSIjwtT%2FIdZQB58VU7HKPpIp1Qqoqf7Vog%3D%3D; uc3=sg2=WvX3PhtDHwnTB6szYiikdAsdGpLEkHN8mOCQDrn5GTo%3D&nk2=D8bhXnHd&id2=UNGXEr3fwoUreg%3D%3D&vt3=F8dBzLgqZ1fEl4mFESM%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTUxNTg5NjA0MQ%3D%3D; uss=WvKV6z8uDwVem1SG1vyqu2tN%2FIk8afcO06NODCrizyWQG7znouFjNfow; sg=689; mt=np=&ci=8_1; cookie1=B0f0IZxeVU68RpwAQ1blVfDWM1YN72shoSZABqnHbD0%3D; unb=3110883738; skt=40adb9c6e23919b8; _l_g_=Ug%3D%3D; _nk_=leet96; cookie17=UNGXEr3fwoUreg%3D%3D; uc1=cookie14=UoTdfkOYuU2m4A%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; isg=ArCw7_BinumkpkL_uDGGqbuCgXfCUZUzQl0YKKoBVYveZVAPUglk0wZVyVP5; v=0; cookie2=1e4b7783c9f5b8d26bb817cafc73e8ac; _tb_token_=e7d4be8b4e313',
    'User Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
    'Referer': 'https://item.taobao.com/item.htm?'
}

def crawler_tb(price_url,comment_url):
    headers = {
        'Cookie': 'cna=2L+FEQUj4hcCAbfAXdikda8c; l=AtnZ9oiWaPSjUUftl30cvcXqac6zxc1b; t=761823bfa80836d34300d5992df1c3b0; thw=cn; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _cc_=WqG3DMC9EA%3D%3D; lgc=leet96; tracknick=leet96; ucn=center; enc=goEeFtR2bToJU1tGj3BOn4uqvnMWyI8UAcA3ubR73wdxpAJfOQ2E%2BSIjwtT%2FIdZQB58VU7HKPpIp1Qqoqf7Vog%3D%3D; uc3=sg2=WvX3PhtDHwnTB6szYiikdAsdGpLEkHN8mOCQDrn5GTo%3D&nk2=D8bhXnHd&id2=UNGXEr3fwoUreg%3D%3D&vt3=F8dBzLgqZ1fEl4mFESM%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTUxNTg5NjA0MQ%3D%3D; uss=WvKV6z8uDwVem1SG1vyqu2tN%2FIk8afcO06NODCrizyWQG7znouFjNfow; sg=689; mt=np=&ci=8_1; cookie1=B0f0IZxeVU68RpwAQ1blVfDWM1YN72shoSZABqnHbD0%3D; unb=3110883738; skt=40adb9c6e23919b8; _l_g_=Ug%3D%3D; _nk_=leet96; cookie17=UNGXEr3fwoUreg%3D%3D; uc1=cookie14=UoTdfkOYuU2m4A%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; isg=ArCw7_BinumkpkL_uDGGqbuCgXfCUZUzQl0YKKoBVYveZVAPUglk0wZVyVP5; v=0; cookie2=1e4b7783c9f5b8d26bb817cafc73e8ac; _tb_token_=e7d4be8b4e313',
        'User Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
        'Referer': 'https://item.taobao.com/item.htm?'
    }
    if re.findall('^https://detailskip.taobao.com',price_url) and re.findall('^https://rate.taobao.com/',comment_url):
        tb_data1=requests.get(url=price_url,headers=headers)
        pr_data=BeautifulSoup(tb_data1.text,'lxml').text
        pr_data_temp= list(set(re.findall('"price":"(.*?)"', pr_data)))
        real_price=sorted(map(float,pr_data_temp))[0]
        #print('评论地址为　%s'%comment_url)
        tb_data2=requests.get(url=comment_url,headers=headers)
        comment_content=BeautifulSoup(tb_data2.text,'lxml').text
        #print(comment_content)
        comment_all=[]
        comment = re.findall('("content":.*?),"rateId"', comment_content)
        for data in comment:
            data=data[11:]
            comment_all.append(data[:-1])
        #print('真实价格为　%s' % real_price)
        # i=1
        # for com in comment_content_data:
        #     print('第 %d 条评论为　%s' % (i,com))
        #     i+=1
        #print('评论为　%s' % comment_content_data)
        totals=re.findall('("total":.*?),"comments"',comment_content)[0]
        total=int(re.findall('(\d+)',totals)[0])
        # print(total)
        # print('第1页的评论为%s '% comment_all)
        i=0
        for data in comment_all:
            i+=1
        # print('第一页的评论数为　%d' % i)
        if i==total:
            print('评论只有一页')
        else:
            for j in range(1,10):
                comment_url = comment_url.replace('currentPageNum=%d'% j, 'currentPageNum=%d' % (j+1))
                tb_data2 = requests.get(url=comment_url, headers=headers)
                comment_content = BeautifulSoup(tb_data2.text, 'lxml').text
                comment_content_data = re.findall('("content":.*?),"rateId"', comment_content)
                u=0
                for data in comment_content_data:
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
        return comment_all

    elif re.findall('^https://mdskip.taobao.com',price_url) and re.findall('^https://rate.tmall.com/',comment_url):
        tb_data1 = requests.get(url=price_url, headers=headers)
        pr_data = BeautifulSoup(tb_data1.text, 'lxml').text
        pr_data_temp = list(set(re.findall('"price":"(.*?)"', pr_data)))
        # print(pr_data_temp)
        real_price = sorted(map(float, pr_data_temp))[0]

        tb_data2 = requests.get(url=comment_url, headers=headers)
        comment_content = BeautifulSoup(tb_data2.text, 'lxml').text
        # print(comment_content)
        pageCounts=re.findall('("lastPage":.*?),"page"',comment_content)
        count=''
        for pageCount in pageCounts:
            count+=pageCount
        count=int(re.findall('\d+',count)[0])
        # print('评论总页数是%d'%count)
        comment_all=[]
        comment= re.findall('("rateContent":.*?),"rateDate"', comment_content)
        for data in comment:
            data=data[15:]
            comment_all.append(data[:-1])
        # print('第1页的评论为%s'% comment_all)

        for i in range(1,count):
            comment_url = comment_url.replace('currentPage=%d'% i, 'currentPage=%d' % (i+1))
            tb_data2 = requests.get(url=comment_url, headers=headers)
            comment_content = BeautifulSoup(tb_data2.text, 'lxml').text
            comment_content_data = re.findall('("rateContent":.*?),"rateDate"', comment_content)
            for data in comment_content_data:
                data = data[15:]
                comment_all.append(data[:-1])
        return comment_all
    else:
        print('无该商品')
        return None

result=crawler_tb(price_url=tb_pri_url,comment_url=tb_com_url)
# print(result)


print('所有评论如下:\n')
# for data in result:
#     print(data)
from pandas import DataFrame
length=len(result)
data=DataFrame(result,columns=['评论'])
print(data)







