'''
Description: 
Version: 
Author: ROING
Date: 2020-11-23 21:57:23
LastEditors: ROING
LastEditTime: 2020-11-27 17:13:26
'''
'''
python解释器在导入模块时，会：
1.搜索当前目录指定模块名的文件，如果有就直接导入
2.如果没有，再搜索系统目录

ps：在开发时，给文件起名，不要和系统的模块文件重名
ps：python中每一个模块（即py文件）都有一个内置属性__file__可以查看模块的完整路径
'''

import random

print(random.__file__)

# 生成一个0~10的数字
rand=random.randint(0,10)
print(rand)