# 请求百度动物识别接口
import base64

# 获取图片的base64
import json

import requests


def Tobase64(path):
    with open(path, "rb") as img_file:
        img_bytes = img_file.read()
        base64_bytes = base64.b64encode(img_bytes)
    return base64_bytes.decode("utf-8")


# 得到图片的base64
base64_str = Tobase64("/home/lzj0726/Desktop/2.jpg")
# 请求百度识图
headers = {"Content-Type": "application/x-www-form-urlencoded"}
para = {"image": base64_str}
print(base64_str)
resp = requests.post(
    "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal?access_token="
    + "24.55ee986fb75277ce21425deb876de626.2592000.1532613276.282335-11445240", headers=headers, data=para)
print(resp.json())
