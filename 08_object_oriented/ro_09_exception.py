'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-15 19:20:41
@LastEditors: Roing
@LastEditTime: 2020-06-15 20:19:08
'''
try:
    num=int(input("请输入一个整数"))
    result = 8 / num
    print(result)

except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")