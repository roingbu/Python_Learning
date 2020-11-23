'''
Description: 
Version: 
Author: ROING
Date: 2020-11-23 21:57:23
LastEditors: ROING
LastEditTime: 2020-11-23 22:15:24
'''
import ro_01_module_test1 as CatModule # 模块别名，大驼峰命名
import ro_02_module_test2

title =CatModule.title

print(title)
CatModule.say_hello()
ro_02_module_test2.say_hello()

wangcai =CatModule.Cat()
waibi = ro_02_module_test2.Dog()
print(wangcai)
print(waibi)
