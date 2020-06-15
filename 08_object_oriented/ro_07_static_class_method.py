'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-14 09:59:47
@LastEditors: Roing
@LastEditTime: 2020-06-14 11:16:08
'''
class Game(object):  # 为了保证保证编写的代码能够同时在 Python 2.x 和 Python 3.x 运行!今后在定义类时,  如果没有父类,  建议统一继承自 object

    top_score = 0

    def __init__(self,name):
        self.player_name = name
        
    @staticmethod
    def show_help():
        print("help tip：let the zombie enter  into house")

    @classmethod
    def game_top_score(cls):  
        
        print("%d is the top score of game"% cls.top_score)


    def start_game(self):
        print("[%s] start the game!"%self.player_name)

zhiwu = Game("roing")
zhiwu.show_help()
zhiwu.game_top_score()
zhiwu.start_game()
