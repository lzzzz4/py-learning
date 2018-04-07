# 获得bilibili相簿的照片
import _thread
import pymysql
import requests

# 连接数据库
import time


def get_json(page):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='linzijie', db='py', charset='utf8')
    # 获取数据库游标
    cursor = conn.cursor()
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      + '(KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        "referer": "https://h.bilibili.com/eden/picture_area"}
    resp = requests.get(
        "https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=" + str(
            page) + "&page_size=20", headers=headers)
    json_text = resp.json()
    # 得到item中的对象
    for data in json_text['data']['items']:
        # 得到上传者的个人信息
        userid = data['user']['uid']
        # print("userid:" + str(userid))
        user_name = data['user']['name']
        # print("username" + str(user_name))
        # 得到一个用户的图片信息
        title = data['item']['title']
        items = data['item']['pictures']
        for item in items:
            src = item['img_src']
            cursor.execute(
                'insert bili_cos(user_id,user_name,title,img_pic,create_time) values(%s,%s,%s,%s,%s)',
                (userid, user_name, title, src, currentTime))
            conn.commit()
            time.sleep(5)
    cursor.close()
    conn.close()


for i in range(1, 5):
    _thread.start_new_thread(get_json, (i,))
    print("开跑!" + str(i))
while True:
    pass
