'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-02 11:07:47
@LastEditors: Roing
@LastEditTime: 2020-06-02 12:35:37
'''
def sum(*args,**kwargs):

    n = 0
    
    for num in args:
        n += num
    
    return n

gl_args = 2,4,1
gl_kwargs = {"fd":"d","ge":"ge"}
number = sum(*gl_args,**gl_kwargs)  # 如果要拆包的话，那么每一个实参前都要分配好 * 或 **
print(type(gl_args))
print(number)