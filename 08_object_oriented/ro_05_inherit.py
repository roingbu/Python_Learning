'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-11 19:46:48
@LastEditors: Roing
@LastEditTime: 2020-06-14 16:29:59
'''

class Animal:
 
    def eat(self):
        print("吃")
 
    def drink(self):
        print("喝")
 
    def run(self):
        print("跑")
 
    def sleep(self):
        print("睡")

class Dog(Animal):

    def bark(self):
        print("wo!")

class XiaoTianQuan(Dog):

    def fly(self):
        print("fly")

    def bark(self):  # this is the way about override!
        print("bark like a god")  
        super().bark()  # 调用父类方法,此处super后面有括号是因为super()是python中特殊的类，这是在创建一个对象
        
        Dog.bark(self)  # 同上，此处Dog后不加括号，因为这在函数中已经存在的对象，这里不需要创建对象。这种方法注意不要调用子类，会造成迭代死循环，所以这种方法不推荐

class cat(Animal):

    def catch(self):
        print("catch mouse")

xtq = XiaoTianQuan()

xtq.bark()

# xtq.catch()  # 显然这样不行233