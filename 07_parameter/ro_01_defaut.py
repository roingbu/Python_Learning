'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-01 21:08:32
@LastEditors: Roing
@LastEditTime: 2020-06-02 11:05:13
'''
def sex(gender=True):
    
    sex_inf = "man" 
    if not gender:
        sex_inf = "girl"
    
    return sex_inf

name = input("name is")
print("%s is %s"%(name,sex()))