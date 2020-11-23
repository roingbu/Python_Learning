'''
@Descripttion: 异常
@version: 
@Author: Roing
@Date: 2020-06-15 19:20:41
LastEditors: ROING
LastEditTime: 2020-11-19 19:46:56
'''
try:
    num=int(input("请输入一个整数"))
    result = 8 / num
    print(result)

except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")