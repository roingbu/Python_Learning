'''
Description: 多态
Version: 
Author: ROING
Date: 2020-11-19 18:22:00
LastEditors: ROING
LastEditTime: 2020-11-19 18:44:42
'''


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s is playing." % self.name)


class XiaoTianQuan(Dog):

    def game(self):  # 对game方法进行重构
        print("%s is playing in the sky." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s and %s are playing." % (self.name, dog.name))

        # let dog play
        dog.game()


wangcai = Dog("旺财")  
wangcai2 = XiaoTianQuan("飞天旺财")
xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(wangcai2)  # 继承和重构 就是多态