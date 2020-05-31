def print_line(char, times):
    """
    print a separator line
    """
    # int(times)  # python会自动根据输入的值判断其类型

    print(char * times)


def print_lines(char, times, lines):  # 当需求多时，尽量不要修改原有函数，而是根据新需求新增一个函数（对象）比较好
    '''
    @description: 打印多行分隔线
    @param char：字符样式
           times：每行个数
           lines：行数
    @return: none
    '''

    i = 0
    while i < lines:
        print(char * times)
        i += 1

name = "Roing"