import os
import types

import requests
import time
from bs4 import BeautifulSoup, Tag

controy_queue = ["波兰", "捷克"]
while controy_queue:
    str_par = controy_queue.pop()
    resp = requests.get("http://www.showguide.cn/showguide/searchNew.php?q=" + str_par)
    resp.encoding = 'utf-8'
    html = resp.text
    bf = BeautifulSoup(html, "html.parser")
    divs = bf.select('div[style="display:none"]')
    for div in divs:
        write_content = ""
        title = div.select("div.searchTitle")
        final_title = ""
        # 得到标题
        if title:
            write_content += "标题:\n\t" + title[0].text + "\n"
            final_title = title[0].text
        img_url = div.select("div.searchFlashpic")
        # 得到图片链接
        if img_url:
            write_content += "图片链接:\n\t" + img_url[0].text + "\n"
        # 得到开始时间
        start_time = div.select("div.searchStime")
        if start_time:
            write_content += "开始时间:\n\t" + start_time[0].text + "\n"
        # 得到详细界面的url
        url = div.select("div.searchArcurl")
        real_url = ""
        if url:
            real_url = "http://www.showguide.cn" + url[0].text
        # 访问详细界面
        if real_url is not "":
            detail_response = requests.get(real_url)
            detail_response.encoding = 'utf-8'
            detail_content = detail_response.text
            # 解析详细界面
            detail_bf = BeautifulSoup(detail_content, "html.parser")
            dlms = detail_bf.select("div.dlm")
            # 遍历第一个dlms
            detail_queue = ['展会介绍', '市场分析', '往届回顾', '展品范围']
            for div_line in dlms[0]:
                if isinstance(div_line, Tag):
                    temp_str = div_line.text.strip().replace("；", "\n")
                    # if temp_str.strip() is not "":
                    if temp_str == "盈拓展览诚邀您参加本届展会，期待与您一起开拓市场，收获无限商机！" \
                                   "更多展会详情请关注外贸局指定展览平台—国际展览导航www.showguide.cn":
                        continue
                    if str(div_line.name) == "h3" or div_line.text.strip() in detail_queue:
                        write_content += temp_str + "\n"
                        continue
                    write_content += "\t" + temp_str + "\n"
                    # findAll = BeautifulSoup(, "html.parser")
                    # h3sps = findAll.find_all("h3 p")
                    # flag = 0

                    # for p in h3sps:
                    #     print(p.text)
                    #     if flag >= 4:
                    #         flag = 3
                    #     if p.text == "友情提示：以上展会信息来源于网络编译，仅供参考。":
                    #         break
                    #     write_content += detail_queue[flag] + ":\n" + p.text + "\n\n"
                    #     flag += 1
            path = "H:/hsy/" + str_par
            if not os.path.exists(path):
                os.mkdir(path)
            final_write_content = write_content.replace("\xa0", "").replace("\uff61", "")
            open(path + "/" + final_title.replace("/", "").replace(" ", "").replace("\uff61", "").strip() + ".txt",
                 "w").write(
                final_write_content)
            time.sleep(2)
    print("success" + str_par)
