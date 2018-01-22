# coding: utf-8
class GrandPa:
    def __init__(self):
        print('I\'m GrandPa')


class Father(GrandPa):
    def __init__(self):
        print('I\'m Father!')


class Son(Father):
    """A simple example class"""
    i = 12345

    def __init__(self):
        print('这是构造函数,son')

    def sayHello(self):
        return 'hello world'


if __name__ == '__main__':
    # son = Son()
    Son()
    print Son().sayHello()
    # 类型帮助信息
    print u'类型帮助信息: ', Son.__doc__
    # 类型名称
    print u'类型名称:', Son.__name__
    # 类型所继承的基类
    print u'类型所继承的基类:', Son.__bases__
    #类型字典
    print u'类型字典:', Son.__dict__
    #类型所在模块
    print u'类型所在模块:', Son.__module__
    #实例类型
    print u'实例类型:', Son().__class__