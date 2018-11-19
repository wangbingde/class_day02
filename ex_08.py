# __new__方法


class MusicPlayer(object):

    # new方法的重写
    def __new__(cls, *args, **kwargs):

        # 1、创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 2、为对象分配空间(调用父类方法，并记录父类返回的引用)
        instance = super().__new__(cls)
        # 3、返回引用
        return instance

    def __init__(self):

        print("初始化")


player = MusicPlayer()
print(player)