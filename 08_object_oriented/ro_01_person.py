'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-05 21:32:42
@LastEditors: Roing
@LastEditTime: 2020-06-05 21:51:06
'''


class Person:

    def __init__(self, name, weight):
        # super().__init__()
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


xiaoming = person("xiaoming", 70)
xiaomei = person("xiaomei", 45)

xiaoming.run()
xiaoming.eat()

xiaomei.run()
xiaomei.eat()

print(xiaoming)
print(xiaomei)
