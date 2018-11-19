# 多态


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在玩耍" % self.name)


class XiaoTian(Dog):

    def game(self):
        print("%s在天上玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        dog.game()


dog = Dog("dog")
xiaotian = XiaoTian("哮天犬")
xiaoming = Person("小明")
xiaoming.game_with_dog(dog)
xiaoming.game_with_dog(xiaotian)
