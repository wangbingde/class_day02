# 类属性和类方法、静态方法


class Tool(object):

    count = 0

    def __init__(self,name):

        self.name = name
        Tool.count += 1

    @classmethod
    def show_tools_count(cls):

        print("工具对象的个数：%d" % cls.count)

    @staticmethod
    def Static():

        print("这是一个静态方法")


tool_1 = Tool("斧头")
tool_2 = Tool("小刀")

# print(Tool.count)
# print(tool_1.count)
# print(tool_2.count)

Tool.show_tools_count()
Tool.Static()
