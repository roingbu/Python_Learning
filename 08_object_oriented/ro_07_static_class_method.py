'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-14 09:59:47
LastEditors: ROING
LastEditTime: 2020-11-19 19:12:04
'''
class Game(object):  # 为了保证保证编写的代码能够同时在 Python 2.x 和 Python 3.x 运行!今后在定义类时,  如果没有父类,  建议统一继承自 object

    top_score = 0

    def __init__(self,name):
        self.player_name = name
        
    @staticmethod  # 定义静态方法，即 既不访问实例属性或方法，也不访问类属性和方法
    def show_help():  # 静态方法不需要指定第一个参数
        print("help tip：let the zombie enter  into house")

    @classmethod
    def game_top_score(cls):  
        
        print("%d is the top score of game"% cls.top_score)


    def start_game(self):
        print("[%s] start the game!"%self.player_name)

Game.show_help()  # 可以通过类名.调用静态方法  -  不需要创建对象
zhiwu = Game("roing")
zhiwu.show_help()  # 这样也可以调用静态方法
zhiwu.game_top_score()
zhiwu.start_game()
