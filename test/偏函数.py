import functools


def int2(x, base=2):
    return int(x, base)


def main():
    print(int('12345'))
    print(int('12345', base=8))
    print(int('12345', base=16))
    # print(int2('1000000'))
    # print(int2('1000000', base=10))
    int3 = functools.partial(int, base=2)  # 相当于 kw={ 'base':2} int('10010', **kw)
    print(int3('10010'))
    max2 = functools.partial(max, 10)
    print(max2(5, 6, 7))

if __name__ == '__main__':
    main()
