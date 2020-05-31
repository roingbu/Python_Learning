'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-05-30 17:02:59
@LastEditors: Roing
@LastEditTime: 2020-05-30 17:08:44
'''
xiaoming = {"age": 12,
            "sex": "man"}

xiaoming2 = {"height": 189}

xiaoming.update(xiaoming2)

print(xiaoming["age"])


for k in xiaoming:
    print("")
