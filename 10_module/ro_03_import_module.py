'''
Description: 
Version: 
Author: ROING
Date: 2020-11-23 21:57:23
LastEditors: ROING
LastEditTime: 2020-11-23 22:30:19
'''
import ro_01_module_test1  # 导入其模块的工具 --- 全局变量、函数、类
import ro_02_module_test2  # 直接import是一次性把模块中所有工具导入，后面from则是导入部分

title = ro_01_module_test1.title

print(title)

ro_01_module_test1.say_hello()
ro_02_module_test2.say_hello()

wangcai = ro_01_module_test1.Cat()
waibi = ro_02_module_test2.Dog()
print(wangcai)
print(waibi)
