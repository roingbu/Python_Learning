'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-14 11:20:00
LastEditors: ROING
LastEditTime: 2020-11-19 19:13:42
'''
class Tool(object):  # 如果类没有指定的父类，就指定（object），这是新式类和旧式类的区别（其实现在指定与否无所谓，主要是为了所写代码在python2中都能运行）

    count = 0  # 这就是类属性，即类内直接定义的赋值语句。类属性通常用于记录类相关的特征，如此处记录创建工具对象的总数

    @classmethod  # 定义类方法
    def show_tool_count(cls):  #类方法的第一个参数是cls，和self类似，用其他也可以，只是习惯cls

        print("The number of tools is %d." % cls.count)

    def __init__(self,name):

        self.name = name

        Tool.count +=1  # 工具类的对象计数+1，实例方法可以访问类属性或类方法

tool1 = Tool("scissors")
tool2 = Tool("shear")
tool3 = Tool("scoop")

tool3.count = 99  # 不推荐，如下

Tool.show_tool_count()
print("工具对象有%d个" % Tool.count)
print("工具对象有%d个" % tool3.count)  # 对象也可以访问类属性，但是对其赋值后并不会影响类属性的值，而只会给对象增加一个属性
print("工具对象有%d个" % tool2.count)  # 如此处，但不推荐这样访问类属性