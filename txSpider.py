import pymysql
import requests
import time
from bs4 import BeautifulSoup

# 连接数据库
conn = pymysql.connect(host='ip', port=3306, user='root', passwd='password', db='db name', charset='utf8')
# 获取数据库游标
cursor = conn.cursor()
currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
newsurl = "http://news.qq.com/"
resp = requests.get(newsurl)

html5Page = resp.text
h5soup = BeautifulSoup(html5Page, "html.parser")
headDiv = h5soup.select("div.head > div.Q-tpList")
for div in headDiv:
    newsHref = div.select("div.Q-tpWrap > a")
    # 新闻连接
    news_href = newsHref[0].get("href")
    imgHref = div.select("div.Q-tpWrap > a > img")
    # 图片链接
    img_href = imgHref[0].get("src")
    textHref = div.select("div.Q-tpWrap > div.text > em > a")
    text_href = textHref[0].text
    cursor.execute(
        'insert news_info(title,create_time,img_url,original_web_url,source,source_id) values(%s,%s,%s,%s,%s,%s)',
        (text_href, currentTime, img_href, news_href, "来自腾讯新闻", 101))
conn.commit()
cursor.close()
conn.close()
