import random  # 导入随机工具包

player = int(input("input your selection， stone (1) / cloth (2) / scissor (3)"))

computer = random.randint(1,3)

print("player select %d ,computer select %d"%(player,computer))

if((player == 1 and computer ==3)
        or (player ==2 and computer ==1)
        or (player ==3 and computer ==2)):
    print("player winning!")
elif(player == computer):
    print("draw")
else:
    print("computer winning!")



