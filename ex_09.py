# 单例实现


class MusicPlayer(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self):

        if MusicPlayer.init_flag is True:
            return
        MusicPlayer.init_flag = True
        print("初始化")


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)