# py 小说写至一章txt
import os

import requests
import time
from bs4 import BeautifulSoup


def search(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      + '(KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    resp = requests.get("http://www.biquge5200.com/modules/article/search.php?searchkey=" + keyword, headers=headers)
    # resp.encoding = 'utf-8'
    # 获得第一本书籍
    html5 = resp.text
    soup = BeautifulSoup(html5, "html.parser")
    trs = soup.select("table.grid > tr")
    # 获取信息列
    tds = trs[1].select("td")
    # 规定格式
    # 书名及链接
    a = tds[0].select("a")
    # 书名链接
    link = a[0].get("href")
    name = a[0].text
    print("书名" + a[0].text + ":" + a[0].get("href"))
    # 最新
    a = tds[1].select("a")
    print("最新章节" + a[0].text + ":" + a[0].get("href"))
    # 作者
    print(tds[2].text)
    # 状态
    print(tds[5].text)
    return [link, name]


link, name = search("斗破苍穹")
# 获取所有章节
resp = requests.get(link)
text = resp.text
soup = BeautifulSoup(text, "html.parser")
# 找出所有的a标签
dds = soup.select("#list > dl > dd")
flag = 0
sum2 = 0
# 取出a的href与text
for dd in dds:
    _as = dd.select("a")
    flag += 1
    if flag >= 10:
        series_one_title = _as[0].text
        print(series_one_title)
        href = _as[0].get("href")
        # 访问页面并获取界面
        resp = requests.get(href)
        # resp.encoding = 'utf-8'
        stext = resp.text
        soup = BeautifulSoup(stext, "html.parser")
        divs = soup.select("#content")
        path = "H:/" + name
        if not os.path.exists(path):
            os.mkdir(path)
        # 将章节写入一个txt文档
        open(path + "/" + name + ".txt", "a").write("\n\n")
        open(path + "/" + name + ".txt", "a").write(series_one_title)
        open(path + "/" + name + ".txt", "a").write("\n\n")
        for line in divs[0]:
            content = str(line).replace("<br/>", "\n\n")
            open(path + "/" + name + ".txt", "a").write(content)
        time.sleep(10)
