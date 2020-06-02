'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-02 17:18:27
@LastEditors: Roing
@LastEditTime: 2020-06-02 18:21:26
'''
s=0
def summ(num):
    
    global s
    
    s = s + num
    if num==1:
        return s
    else:
        
        n= summ(num-1)
        return n
        
print(summ(2))
    