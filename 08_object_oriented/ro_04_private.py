'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-10 20:24:59
LastEditors: ROING
LastEditTime: 2020-11-19 12:37:41
'''


class Woman:

    def __init__(self, name, age):

        self.name = name
        self.__age = age  # 在对象前加两个 “_” ,就是私有属性

    def __str__(self):

        return ("%s is %d years old." % (self.name, self.__age))

    def __secret(self):  # # 在方法前加两个 “_” ,就是私有方法

        print("%s is %d years old." % (self.name, self.__age))

    def tell(self):

        self.__secret()  # 在对象的方法内部, 是可以访问对象的私有方法


xiaofang = Woman("xiaofang", 19)

# print(xiaofang.__age)  私有属性, 在外界不能够直接访问
print("-----------------------")
# xiaofang.__secret  私有方法, 在外界不能够直接访问
print("-----------------------")
print(xiaofang)
print("-----------------------")
xiaofang.tell()
print("-----------------------")

print(xiaofang._Woman__age)  # 伪私有属性和私有方法(科普不推荐使用),这种方法可以强行调用私有属性或方法
xiaofang._Woman__secret()
