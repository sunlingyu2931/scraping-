# HTTP 超文本传输协议（HTTP，HyperText Transfer Protocol)是互联网上应用最为广泛的一种网络协议
# 一种基于"请求与响应"模式的、无状态的应用层协议

import requests  # 获取页面
from bs4 import BeautifulSoup # 解析parser

# 获取url
def getHTML(url):
    try:
        r = requests.get(url)  # 请求获得url的位置
        r.raise_for_status()  # 200是成功获取url
        print('get html successfully')
        r.encoding = 'utf-8' # header中可以找到响应内容的编码方式
        return r.text
    except:
        return ''

# 解析
def parseHTML(html):
    try:
        soup = BeautifulSoup(html,'html.parser')
        A = soup.find_all('span',attrs={'class':'short'})  # review存放的位置
        B =[]
        for i in A:
            B.append(i.get_text())
        return B
    except:
        return []


def main():
    discuss = []
    a = 0
    for i in range(0,4,20):  # 爬取4页，每页20条，从url的形式可以看出
        url = 'https://movie.douban.com/subject/26100958/comments?start=' + str(i) + '&limit=20&sort=new_score&status=P'
        HTMLpage = getHTML(url)
        for t in parseHTML(HTMLpage):
            discuss.append(t)
    for i in discuss:
        print(str(a)+':'+i)
        a = a + 1

if __name__ == '__main__':
    main()
