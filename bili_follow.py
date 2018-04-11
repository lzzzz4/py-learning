# 多线程爬取
# https://api.bilibili.com/x/relation/stat?vmid=63231&jsonp=jsonp&callback=__jp3
# 获取粉丝总数

# https://api.bilibili.com/x/relation/followers?vmid=63231&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp20
# 获取粉丝数据



# 获取粉丝总数
import json
import random

import _thread
import pymysql
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) '
                  + 'Version/10.0 Mobile/14E304 Safari/602.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    , 'Host': 'api.bilibili.com'
}
#携带的cookie
cookies = {xxx}
task_pool = []
run_status = [True, True, True, True, True, True]


def count_follow_people(uid):
    resp = requests.get("https://api.bilibili.com/x/relation/stat?vmid=" + str(uid) + "&jsonp=jsonp&callback=__jp3",
                        headers=headers)
    resp.encoding = 'utf-8'
    follow_jsonp = resp.text
    start = follow_jsonp.find("(")
    end = len(follow_jsonp)
    follow_json = json.loads(follow_jsonp[start + 1:end - 1])
    # 获得粉丝总数
    follow_count = follow_json['data']['follower']
    return follow_count


def list_follow_info(uid, task):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='linzijie', db='py', charset='utf8')
    # 获取数据库游标
    cursor = conn.cursor()
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    follow_info_html = requests.get(
        "https://api.bilibili.com/x/relation/followers?vmid=" + str(uid) + "&pn=" + str(task) +
        "&ps=20&order=desc&jsonp=jsonp&callback=__jp20",
        headers=headers, cookies=cookies)
    follow_info_html.encoding = 'utf-8'
    follow_info_jsonp = follow_info_html.text
    start = follow_info_jsonp.find("(")
    end = len(follow_info_jsonp)
    follow_info_json = json.loads(follow_info_jsonp[start + 1:end - 1])
    for info in follow_info_json['data']['list']:
        uid = info['mid']
        uname = info['uname']
        sign = info['sign']
        vip_type = info['vip']['vipType']
        cursor.execute(
            'insert bili_follow(uid,uname,sign,vip_type,create_time) values(%s,%s,%s,%s,%s)',
            (uid, uname, sign, vip_type, currentTime))
        conn.commit()
        time.sleep(0.1)
    cursor.close()
    conn.close()


def page_num(follow):
    d = follow / 20
    d = int(d)
    if follow % 20 != 0:
        d += 1
    for j in range(d, 0, -1):
        task_pool.append(j)


def dispatch_task(taskid, uid):
    while task_pool:
        task = task_pool.pop()
        list_follow_info(uid, task)
        origin_sleep = random.uniform(2, 5)
        sleep_time = ("%.2f" % origin_sleep)
        time.sleep(sleep_time)
    run_status[taskid] = False


# 获得粉丝总数
follow_count = count_follow_people(63231)
# 初始化任务池
page_num(follow_count)
# 获取粉丝信息  63231
want_id = 63231
for i in range(1, 6):
    _thread.start_new_thread(dispatch_task, (i, want_id,))
    print(i, "running!")
while bool(run_status[1]) or bool(run_status[2]) or bool(run_status[3]) or bool(run_status[4]) or bool(run_status[5]):
    pass
