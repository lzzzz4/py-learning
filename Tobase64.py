# img转化为base64
import base64

file = open("/home/lzj0726/Pictures/time.jpg", 'rb')
base64str = base64.b64encode(file.read())
#print(base64str)
open("/home/lzj0726/Desktop/1.txt", "wb").write(base64str)
file.close()
# 读取base64
#with open("/home/lzj0726/Desktop/1.txt", 'r') as bs_file:
#    bs_str = bs_file.read()
#print(bs_str)
#img = open("/home/lzj0726/Desktop/1.jpg", 'wb').write(base64.urlsafe_b64decode(bs_str))
