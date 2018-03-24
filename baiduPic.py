import requests
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  + '(KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36', "referer": "https://image.baidu.com"}
word = "美女"
word = urllib.parse.quote(word)
width = 100
height = 100
# 从第几个图片开始
pn = 0# 显示几个
rn = 30
params = {"tn": "resultjson_com", "ipn": "rj", "ct": "201326592", "fp": "result", "ie": "utf-8", "oe": "utf-8",
          "word": word, "width": width, "height": 100, "pn": pn, "rn": rn, "gsm": "30000001d"}
resp = requests.get("https://image.baidu.com/search/acjson"
                    + "?tn=resultjson_com&fp=result&ie=utf-8&oe=utf-8&ipn=rj"
                    + "&word=" + word + "&width=" + str(width) + "&height=" + str(height)
                    + "&pn=" + str(pn) + "&rn=" + str(rn), headers=headers)
# resp = requests.get("https://image.baidu.com/search/acjson", data=params, headers=headers)
print(resp.url)
resp.encoding = 'utf-8'
json = resp.json()
print(json)
for data in json['data']:
    try:
        if data['thumbURL'][8:11].find("ss") >= 0:
            print(data['thumbURL'])
            print(data['fromPageTitle'])
    except:
        pass
