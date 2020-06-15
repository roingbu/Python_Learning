'''
@Descripttion: 
@version: 
@Author: Roing
@Date: 2020-06-14 11:20:00
@LastEditors: Roing
@LastEditTime: 2020-06-14 11:27:37
'''
class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):

        print("The number of tools is %d." % cls.count)

    def __init__(self,name):

        self.name = name

        Tool.count +=1

tool1 = Tool("scissors")
tool2 = Tool("shear")
tool3 = Tool("scoop")

Tool.show_tool_count()