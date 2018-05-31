# 执行控制台输入
import os
import time
import xml.etree.ElementTree as ET

# 解析xml
from xml import etree

dir_path = input('请输入xml文件的父路径(复制完整路径)：')
if not os.path.isdir(dir_path):
    print("请检查路径!")
    time.sleep(1.5)
    exit()
# 如果路径为文件夹
if os.path.isdir(dir_path):
    # 将格式统一
    if dir_path[len(dir_path) - 1] == "/":
        dir_path = dir_path[0:len(dir_path) - 1]
    label = input("请输入要将label替换为什么")
    file_list = os.listdir(dir_path)
    print("正在遍历xml文件...")
    # 遍历文件夹
    for file in file_list:
        if os.path.splitext(file)[1] == '.xml':
            fin_path = dir_path + "/" + file
            print("正在操作" + fin_path)
            tree = ET.parse(fin_path)
            root = tree.getroot()
            for d in root.findall("object"):
                name = d.find("name")
                # print(name.text)
                name.text = label
            tree.write(fin_path, encoding="utf-8")
print("----------------------------ok----------------------------")
print("success!!!")
time.sleep(10)
