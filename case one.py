from bs4 import BeautifulSoup
import requests

url = requests.get('https://redditmetrics.com/top')

soup = BeautifulSoup(url.text, 'html.parser')

with open('/Users/sunlingyu/Desktop/sc.txt', 'w') as f:
    for subreddit in soup.find_all('a'):
        try:
            if '/r' in subreddit.string:   #只读前100个，不再翻页
                f.write(subreddit.string[3:] + '\n')  #只从第三个开始读，不读/r/
        except:
            TypeError