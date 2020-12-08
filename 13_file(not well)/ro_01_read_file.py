'''
Description: 
Version: 
Author: ROING
Date: 2020-12-03 21:49:07
LastEditors: ROING
LastEditTime: 2020-12-03 21:58:30
'''


# 在开发中，通常会先编写打开和关闭的代码，再编写中间针对文件的读/写操作!

# 1. open file
# open()默认以 只读方式 打开文件
file = open("test")  # 第一次打开文件时，通常文件指针会指向文件的开始位置

# 文件名要注意区分大小写

# 2. read file
text = file.read()  # 当执行了 read 方法后文件指针会移动到读取内容的末尾
print(text)
print(len(text))

print("-"*50)

text = file.read()
print(text)
print(len(text))

# 3. close file
file.close()  # 打开方法写好后，记得关闭