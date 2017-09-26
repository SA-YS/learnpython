def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


def count():
    # fs = []
    # for i in range(1, 4):
    #     def f():
    #         return i * i
    #     fs.append(f)
    # return fs
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


def main():
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f())
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)  # False
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())


if __name__ == '__main__':
    main()

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
