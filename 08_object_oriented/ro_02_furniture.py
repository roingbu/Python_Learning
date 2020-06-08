'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-06 12:22:35
@LastEditors: Roing
@LastEditTime: 2020-06-08 16:10:11
'''
class HouseItem:

    def __init__(self,name,area):

        self.name = name
        self.area = area
        
    def __str__(self):

        return "[%s] 占地 %.2f" % (self.name, self.area)

class House:

    def __init__(self,house_type, area):
        
        self.house_type = house_type
        self.area = area

        #剩余面积
        self.free_area = area
        #家具名称列表
        self.item_list = []

    def __str__(self):

        return ("户型： %s\n总面积：%.02f[剩余：%.2f]\n家具：%s"
                %(self.house_type,self.area,
                self.free_area,self.item_list))
    
    def add_item(self, item):

        print("要添加 %s"%item)
        
        #判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大，无法添加" % item.name)
            return
        
        self.item_list.append(item.name)

        self.free_area -= item.area

bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

Gou_house = House("三室一厅", 170)

Gou_house.add_item(bed)
Gou_house.add_item(chest)
Gou_house.add_item(table)

print(Gou_house)

print(type(bed))

