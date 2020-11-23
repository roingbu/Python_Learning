'''
@Descripttion: 单例设计模式
@version: 
@Author: Roing
@Date: 2020-06-14 16:00:27
LastEditors: ROING
LastEditTime: 2020-11-19 19:46:11
'''
class MusicPlayer(object):
    
    instance = None  # 记录第一个被创建对象的引用
    init_flag = False  # 记录是否执行过初始化动作
    
    def __new__(cls):  # 内置的静态方法，为对象分配内存空间，返回对象的引用 -- 重写__new__方法的代码非常固定！！，并且需要主动传递参数cls 
        # location = super().__new__(cls)
        # return location
        # return super().__new__(cls)

        # 以下就是单例设计模式
        if MusicPlayer.instance is None:  # 判断类属性是否是空对象
            
            print("创建对象，分配空间")
            MusicPlayer.instance = super().__new__(cls)  # 调用父类方法，为第一个对象分配空间
            return MusicPlayer.instance
            
        return MusicPlayer.instance  # 还没完，以下内置方法的重写也是单例设计模式
        
    def __init__(self):
        
        # if MusicPlayer.init_flag == False:
            
        #     print("initialize the player")
        #     MusicPlayer.init_flag = True
        #     return
        
        #此处
        if MusicPlayer.init_flag:
            return
            
        print("initialize the player")
        MusicPlayer.init_flag = True
            
player1 = MusicPlayer()
# print(dir(MusicPlayer))
print(player1)

player2 = MusicPlayer()
print(player2)