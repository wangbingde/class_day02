# 父类的私有属性和私有方法


class A:

    def __init__(self):
        self.num1 = 10
        self.__num2 = 100

    def test(self):
        print("成绩1是%d" % self.num1)
        print("成绩2是%d" % self.__num2)

    def __test(self):
        print(self.num1)
        print(self.__num2)


class B(A):

    def demo(self):
        print(self.num1)


b = B()
print(b.num1)
b.test()
b.demo()
