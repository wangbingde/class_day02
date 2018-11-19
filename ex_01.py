# 单继承


class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡--")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")



class XiaoTian(Dog):

    def fly(self):
        print("会飞")




wangcai =Dog()
wangcai.sleep()
wangcai.bark()
xiao=XiaoTian()
xiao.bark()
xiao.fly()