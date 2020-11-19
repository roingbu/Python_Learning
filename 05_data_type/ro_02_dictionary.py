'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-05-30 17:02:59
LastEditors: ROING
LastEditTime: 2020-11-16 15:54:31
'''
xiaoming = {"age": 12,
            "sex": "man"}

xiaoming2 = {"height": 189}

xiaoming.update(xiaoming2)

print(xiaoming["age"])


for k in xiaoming:
    print(k)
    print("")
