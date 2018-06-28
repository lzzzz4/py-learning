# 请求百度车型识别接口
import requests

from ai.baidu_animal_ai import baidu_animal


class baidu_car:
    # 请求
    def requestAi(para, purl):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(purl + "?access_token="
                             + "24.55ee986fb75277ce21425deb876de626.2592000.1532613276.282335-11445240",
                             headers=headers,
                             data=para)
        print(resp.json())
    
    if __name__ == '__main__':
        base_64_str = baidu_animal.Tobase64("/home/lzj0726/Desktop/timg.jpg")
        para = {"image": base_64_str}
        requestAi(para, "https://aip.baidubce.com/rest/2.0/image-classify/v1/car")
