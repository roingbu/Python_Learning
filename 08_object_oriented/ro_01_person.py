'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-05 21:32:42
LastEditors: ROING
LastEditTime: 2020-11-19 12:37:00
'''


class Person:

    def __init__(self, name, weight):
        # super().__init__()  # super（）调用父类方法
        self.name = name
        self.weight = weight

    def __str__(self):

        return "%s's weight is %.2f kg." % (self.name,
                                            self.weight)

    def run(self):

        print("%s love running" % self.name)
        self.weight -= 1

    def eat(self):

        print("%s like eating" % self.name)
        self.weight += 2


xiaoming = Person("xiaoming", 70)
xiaomei = Person("xiaomei", 45)

xiaoming.run()
xiaoming.eat()

xiaomei.run()
xiaomei.eat()

print(xiaoming)
print(xiaomei)
