'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-14 16:00:27
@LastEditors: Roing
@LastEditTime: 2020-06-14 16:56:38
'''
class MusicPlayer(object):
    
    quote = None
    init_flag = False
    
    def __new__(cls):
        # location = super().__new__(cls)
        # return location

        # return super().__new__(cls)

        if MusicPlayer.quote is None:

            MusicPlayer.quote = super().__new__(cls)
            return MusicPlayer.quote
            
        return MusicPlayer.quote
        
    def __init__(self):
        
        # if MusicPlayer.init_flag == False:
            
        #     print("initialize the player")
        #     MusicPlayer.init_flag = True
        #     return
        
        if MusicPlayer.init_flag:
            return
            
        print("initialize the player")
        MusicPlayer.init_flag = True
            
player1 = MusicPlayer()
# print(dir(MusicPlayer))
print(player1)

player2 = MusicPlayer()
print(player2)