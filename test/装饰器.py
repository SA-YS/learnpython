# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
import functools


def log(fun):
    def wrapper(*args, **kw):
        print('call %s();' % fun.__name__)
        return fun(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            if isinstance(text, str):
                print('call %s %s:' % (text, func.__name__))
            else:
                print('call %s:' % func.__name__)
            func(*args, **kw)
            print('end call')
            return
        return wrapper
    return decorator(text) if callable(text) else decorator


@log3('12345')
def now(s, v):
    print(s, v)


def main():
    # f = now
    # f()
    # print(f.__name__)
    # print(now.__name__)
    now('hello', v='world')
    # print(now.__name__)


if __name__ == '__main__':
    main()
