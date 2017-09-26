def build(x, y):
    return lambda: x * x + y * y  # 匿名函数可以作为返回值返回


def main():
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    f = lambda x: x * x
    print(f, f(5))

if __name__ == '__main__':
    main()