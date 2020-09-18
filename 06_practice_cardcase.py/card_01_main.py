# ！ C:/Users/76948/AppData/Local/Microsoft/WindowsApps/python3.exe
'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-05-31 15:11:14
@LastEditors: Roing
@LastEditTime: 2020-06-01 11:15:56
'''
import card_02_tools

while True:

    card_02_tools.show_menu()
    inp = input("请选择您需要的功能")
    print("您选择的功能是：【%s】" % inp)

    if inp in ["1", "2", "3"]:

        if inp == "1":  # (roing) 新增名片
            # pass
            card_02_tools.new_card()
        if inp == "2":  # show all
            card_02_tools.show_all()
        if inp == "3":  # search card
            # pass
            card_02_tools.search_card()
    elif inp == "0":
        break
    else:
        print("请选择您需要的功能")
