'''
Description: 
Version: 
Author: ROING
Date: 2020-11-19 18:08:40
LastEditors: ROING
LastEditTime: 2020-11-19 18:08:40
'''
class A:
    
    def test(self):
        print("This is test a.")
    # pass  # 类不能空，用pass做一个占位


class B:

    def test(self):
        print("This is test b.")
    # pass


class C(A, B):  # 多继承中如果有重名的方法，按从左至右优先级检索，如此处是用A的方法
    pass

test1 = C()
test1.test()