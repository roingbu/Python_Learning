'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-05-31 15:11:24
LastEditors: ROING
LastEditTime: 2020-09-14 09:44:47
'''
card_list = []


def show_menu():
    '''
    @description: 显示菜单
    @param {type} 
    @return: 
    '''
    print("*"*50)
    print("【1】new card")
    print("【2】show all")
    print("【3】search card")
    print("")
    print("【0】exit")
    print("*"*50)


def new_card():
    '''
    @description: 新增名片
    @param {type} 
    @return: 
    '''
    print("-"*50)
    print("【1】new card")
    name = input("请输入姓名: ")
    phone = input("请输入电话: ")
    qq = input("请输入QQ: ")
    email = input("请输入邮箱: ")

    card_dict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }

    card_list.append(card_dict)

    print("card appended succussfully")
    print("new card is%s" % card_dict)


def show_all():
    '''
    @description: 显示全部
    @param {type} 
    @return: 
    '''
    print("-"*50)
    print("【2】show all")

    if len(card_list) == 0:
        print("none of card")
        return

    for name in ["name", "phone", "qq", "email"]:
        print(name, end="\t\t")

    print("")

    print("="*30)

    for card_dict in card_list:
        for item in card_dict:

            print(card_dict[item], end="\t\t")
        print("")


def search_card():
    '''
    @description: 搜索名片
    @param {type} 
    @return: 
    '''
    print("-"*50)
    print("【3】search card")

    find_name = input("input the name you want to search")

    for card_dict in card_list:
        if card_dict["name"] == find_name:

            print("name\t\tphone\t\tqq\t\temail")
            print("="*30)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

            deal_card(card_dict)

            break
        else:

            print("sorry,can't find it")


def deal_card(find_dict):
    '''
    @description: edit & remove card 
    @param {dictionary} find_dict:searched card 
    '''

    action_str = input("input the operation you want:"
                       "1.edit 2.remove 0.return to menu")

    if action_str == "1":
        find_dict['name'] = input_card_info(find_dict['name'], 'name')
        find_dict['phone'] = input_card_info(find_dict['phone'], 'phone')
        find_dict['qq'] = input_card_info(find_dict['qq'], 'qq')
        find_dict['email'] = input_card_info(find_dict['email'], 'email')

        print("edit successfully")
    elif action_str == "2":
        card_list.remove(find_dict)

        print("remove successfully")


def input_card_info(original_dict, tip):
    '''
    @description: 输入字典的值
    @param {str}: original_dict 原字典相应key的值 
    @param {str}: tip 提示要输入的值的key
    @return: 如果不输入任何值，输出原值；否则输出改变的值
    '''

    result_str = input(tip)

    if len(result_str) > 0:
        return result_str

    else:
        return original_dict
