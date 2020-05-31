'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-05-31 10:51:46
@LastEditors: Roing
@LastEditTime: 2020-05-31 11:06:12
'''

"""
# items = [1, 2, 3]
# for item in items:
#     print("list中有%d"%item)
#     if item == 2:
#         break
# else:
#     print("123")


# print("循环结束")
"""

student = [
    {"name":"mei",
    "sex":"girl"},
    {"name":"wang",
    "sex":"man"}
]

find_name = "mei"

for info in student:
    print(info)
    if info["name"] == find_name:
        print("find %s!"%find_name)
        break
else:
    print("can't find %s !"%find_name)

print("cycle breaks")


 
