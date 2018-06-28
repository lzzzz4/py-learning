# 商品logo识别

from ai.baidu_animal_ai import baidu_animal
from ai.baidu_car_ai import baidu_car


class baidu_logo:
    if __name__ == '__main__':
        # 图片的路径
        base_64_str = baidu_animal.Tobase64("/home/lzj0726/Desktop/timg.jpg")
        baidu_car.requestAi({"image": base_64_str}, "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo")
