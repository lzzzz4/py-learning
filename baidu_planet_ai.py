# 百度植物识别
from ai.baidu_animal_ai import baidu_animal
from ai.baidu_car_ai import baidu_car

base64_str = baidu_animal.Tobase64("/home/lzj0726/Desktop/timg.jpg")
baidu_car.requestAi({"image": base64_str}, "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant")
