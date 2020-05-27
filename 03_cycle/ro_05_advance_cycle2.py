# 定义行变量
row = 1
 
while row <= 9:
    # 1. 定义一个列计数器变量
    col = 1
    # 2. 开始循环
    while col <= row:
        # print("%d" % row)
        # 每一行打印多少个小星星
        # print("%d"% row, "x", "%d"%col, "=", row * col, end="   ")  # 1st method
        print("%dx%d="%(row,col),row* col,end="\t")  # 2nd method  # \t 制表符，协助在输出文本时 垂直方向保持对其
        print("%dx%d=%d"%(row,col,row* col),end="\t")  #3rd method 
        col += 1
    # print("第 %d 行" % row)
    # 这行代码就是在一行星星输出完之后, 添加换行 !
    print("")
    row += 1