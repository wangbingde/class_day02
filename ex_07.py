# 方法综合案例


class Game(object):

    top_score = 0

    def __init__(self,name):

        self.name = name

    @staticmethod
    def show_help():
        print("帮助信息")

    @classmethod
    def show_top_score(cls):

        print("历史最高得分：%d" % cls.top_score)

    def start_game(self):

        print("%s的游戏开始了..." % self.name)


Game.show_help()
Game.show_top_score()
player_name = input("输入玩家姓名：")
player = Game(player_name)
player.start_game()