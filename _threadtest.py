# 多线程测试
import _thread

import time


def sb(threadName, parameter):
    while True:
        parameter += 1
        print(threadName + ":" + str(parameter))
        time.sleep(0.5)


try:
    _thread.start_new_thread(sb, ("lzj1", 1,))
    _thread.start_new_thread(sb, ("lzj2", 10,))
    time.sleep(3)
except Exception as e:
    print(e)
# 主线程不会死
while True:
    pass
