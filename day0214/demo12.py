'''
类装饰器
'''


class Abc():

    def __init__(self,fun):
        print("方法1")
        self.f=fun

    def __call__(self, *args, **kwargs):
        print("call")
        self.f()

# cu=Abc()
# 实例名加（）会执行call方法
# cu()


@Abc
def show():
    print("类装饰器")

show()

'''
类装饰器通过构造方法和call方法实现
当程序检测到函数有类装饰器时没有直接执行函数，将函数作为参数传递给类的装饰器
当该函数调用时会执行call方法

'''