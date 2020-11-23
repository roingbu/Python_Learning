'''
@Descripttion:
@version:
@Author: Roing
@Date: 2020-06-05 21:32:42
LastEditors: ROING
LastEditTime: 2020-11-19 20:46:40
'''



class Person:

    def __init__(self, name, weight):  # 前后两个下划线的方法是 内置方法
        # super().__init__()  # super（）指调用父类方法，此处是类的父类方法，即是python中新式类的内置方法
        self.name = name
        self.weight = weight

    def __str__(self):  # print类创建的对象时，触发的方法

        return "%s's weight is %.2f kg." % (self.name,
                                            self.weight)

    def run(self):

        print("%s love running" % self.name)
        self.weight -= 1

    def eat(self):

        print("%s like eating" % self.name)
        self.weight += 2

# 创建出来的对象是类的实例，如xiaoming是Person的一个实例
# 创建对象的动作，就是实例化
# 对象的属性，是实例属性
# 对象的方法，是实例方法
xiaoming = Person("xiaoming", 70)
xiaomei = Person("xiaomei", 45)

xiaoming.run()
xiaoming.eat()

xiaomei.run()
xiaomei.eat()

# 每一个对象都有自己独立的内存空间，保存各自不同的属性
# 多个对象的方法，在内存中只有一份。在调用方法时，需要把对象的引用传递到方法内部

print(xiaoming)
print(xiaomei)
