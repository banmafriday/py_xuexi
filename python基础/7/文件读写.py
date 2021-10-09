# coding:utf-8
# 读文件

f = r"C:\Users\ban\Desktop\t1.txt"
file = open(f, "r", encoding="utf-8")
data = file.read()
file.close()

a = ""
b = ""
for i in data:

    if i == data:
        print("1")
