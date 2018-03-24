import json
import os
import uuid

import requests

# 热门作品推荐
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  + '(KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
# index第几页 page为8,官方调用写死为8 表示一页几个歌手
index = "20"
resp = requests.get("http://cgi.kg.qq.com/fcgi-bin/fcg_homepage_feed?index=" + index + "&page=8", headers=headers)
# 得到json字符串
# resp.encoding = "utf-8"
organizeJson = resp.text
start = organizeJson.find("{")
end = organizeJson.rfind(")")
myjson = organizeJson[start:end]
myjson = json.loads(myjson)
# print(myjson['data']['feeds'])
for data in myjson['data']['feeds']:
    print("演唱者昵称" + data['nick'])
    print("性别" + data['sex'])
    url = "https://kg.qq.com/node/play?s=" + data['share_url'] + "&g_f=share_html"
    print("歌曲名" + data['songname'])
    # 得到歌曲的url访问并下载
    songMain = requests.get(url, headers=headers)
    html5 = songMain.text
    tempstart = html5.find("playurl")
    #  print("开始" + str(tempstart))
    end = html5.find("playurl_video")
    #  print("结束" + str(end))
    # 得到歌曲下载的url
    songurl = html5[tempstart + 10:end - 3]
    flag = 1
    if songurl == "":
        # print("songurl为空需要去video获取")
        tempstart = html5.find("playurl_video")
        end = html5.find("poi_id")
        songurl = html5[tempstart + 16:end - 3]
        flag = 0
    music = requests.get(songurl, headers)
    if music.status_code == 200:
        path = "H:/qqkg"
        if not os.path.exists(path):
            os.mkdir(path)
        if flag == 0:
            open(path + "/" + str(uuid.uuid1())[0:10] + str(data['songname']) + ".mp4",
                 "wb").write(
                music.content)
        else:
            open(path + "/" + str(uuid.uuid1())[0:10] + str(data['songname']) + ".m4a",
                 "wb").write(
                music.content)
