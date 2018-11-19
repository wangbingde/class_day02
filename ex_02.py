# 方法的重写


class Animal:

    def eat(self):
        print("吃--")

    def drink(self):
        print("喝--")

    def run(self):
        print("跑--")

    def sleep(self):
        print("睡--")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTian(Dog):

    def fly(self):
        print("会飞")

    def bark(self):
        # 针对需求，编写子类特定代码
        print("嗷嗷")
        # 通过super()调用父类方法
        # super().bark()
        Dog.bark(self)


# wangcai = Dog()
# wangcai.sleep()
# wangcai.bark()
xiao = XiaoTian()
xiao.bark()
xiao.fly()
