from functools import reduce  # python3


def f(x):
    return x*x


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def user_input(names):
    def normailze(name):
        return name.lower().capitalize()
    return list(map(normailze, names))


def prod(L):
    return reduce(lambda x, y : x * y, L)


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    ss = s.split('.')
    return reduce(lambda x, y: 10 * x + y, map(char2num, ss[0])) + reduce(lambda x, y: 10 * x + y,
                                                                          map(char2num, ss[1])) * 0.1 ** len(ss[1])


def main():
    # r = map(f, [1, 2, 3])
    # print(list(r))
    # s = reduce(add, [1, 3, 5, 7, 9])
    # print(s)
    # print(reduce(fn, [1, 3, 5, 7, 9]))
    # print(str2int('123'), type(str2int('123')))
    # names = ['adam', 'LISA', 'barT']
    # print(user_input(names))
    print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
    print(str2float('123.456'))

if __name__ == '__main__':
    main()
