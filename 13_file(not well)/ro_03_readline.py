'''
Description: 
Version: 
Author: ROING
Date: 2020-12-03 22:07:20
LastEditors: ROING
LastEditTime: 2020-12-03 22:10:09
'''
file = open("test")

while True:
    text=file.readline()  # 一行一行往下读取
    
    # 判断是否读取到内容
    if not text:
        break

    print(text)

file.close()