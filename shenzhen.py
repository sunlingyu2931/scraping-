from bs4 import BeautifulSoup
import requests
import time

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
# 注意这里是字典形式，还要写user-agent

def judgment_sex (class_name): # 因为这个网页的男女不是文字，是图片形式显示的所以我们需要define一个函数来判断一下
    if class_name == ['member_icol']:
        return 'girl'
    else:
        return 'boy'

def get_links(url):   # 进入各个新的link的函数
    wb_data = requests.get(url, headers=headers) # 获取url
    soup = BeautifulSoup(wb_data.text, 'lxml')  # 解析
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get('href')
        get_info(href)

def get_info(url):    # 进入新的link后的具体信息的获取
    wb_data = requests.get(url,headers=headers)    # 获取url
    soup = BeautifulSoup(wb_data.text,'lxml')       # 解析
    tittles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    images = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')

    for tittle,address,price, image, name, sex in zip(tittles,addresses,prices,images,names,sexs):
        data = {'tittle':tittle.get_text().strip(),
                'address':address.get_text().strip(),
                'price':price.get_text().strip(),
                'image':image.get_text().strip(),
                'name':name.get_text().strip(),
                'sex':judgment_sex(sex.get('class'))}
        print(data)

if __name__ == '__main__':
    urls = ['http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,3)] #爬取1-3页
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)  # 循环一个页面然后休息2s






