'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-02 17:18:27
@LastEditors: Roing
@LastEditTime: 2020-06-02 18:25:35
'''
# s=0
def summ(num):
    
    # global s
    
    # s = s + num
    if num==1:
        return 1
    
    temp = summ(num-1)
    
    return temp + num
print(summ(2))
    