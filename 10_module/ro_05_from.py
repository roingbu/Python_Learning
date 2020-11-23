'''
Description: 
Version: 
Author: ROING
Date: 2020-11-23 21:57:23
LastEditors: ROING
LastEditTime: 2020-11-23 22:40:43
'''
# 从 模块 导入 工具名
from ro_02_module_test2 import Dog # 如此可以导入该模块中的部分工具
from ro_01_module_test1 import say_hello
from ro_02_module_test2 import say_hello  # 如此，若存在同名函数，后者覆盖前者
from ro_01_module_test1 import say_hello  as Say1  # 此时只要取一个别名即可

# from ro_01_module_test1 import *  # 这样也可以导入所有工具，而且使用工具时不需要通过 模块名.
# 注意：from xxx import * 这种方式不推荐使用，因为函数重名并没有任何提示，出现问题难以排查

say_hello()  # 不需要通过 模块名. ，直接用
Say1()

waibi = Dog()
print(waibi)
