from lxml import etree

import requests

# dom = xml.dom.minidom.
# ds = dom.getElementsByTagName("d")
# for d in ds:
#     print("%s" % d.firstChild.data)
resp = requests.get("https://comment.bilibili.com/36701006.xml")
resp.encoding = 'utf-8'
page = etree.HTML(resp.content)
ds = page.xpath("//i/d")
for d in ds:
    print(d.text)
