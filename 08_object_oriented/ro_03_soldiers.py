'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-10 11:17:57
LastEditors: ROING
LastEditTime: 2020-11-19 12:32:27
'''


class Gun:

    def __init__(self, model):

        self.model = model
        self.ammo = 0

    def add_ammo(self, count):

        self.ammo += count

    def shoot(self):

        if self.ammo <= 0:
            print("no bullet")

            return

        self.ammo -= 1
        print("%s Tu [%dremained]" % (self.model, self.ammo))


class Soldier:

    def __init__(self, name):

        self.name = name
        self.gun = None  # 在不知道啥数据类型

    def fire(self):

        if self.gun is None:
            print("[%s]no gun" % self.name)

            return

        print("[%s] SAY:go,go,let's go!" % self.name)

        # self.gun.add_ammo(67)

        self.gun.shoot()


ak47 = Gun("ak47")
ak47.add_ammo(67)
ak47.shoot()

xusanduo = Soldier("xusanduo")

xusanduo.gun = ak47
xusanduo.fire()
