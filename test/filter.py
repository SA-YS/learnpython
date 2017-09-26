def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


# 从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选序列
def _not_divisible(n):
    return lambda x: x % n > 0


# 生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def main():
    # print(list(filter(is_odd, [1, 2, 3, 4, 5])))
    # print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
    # 打印1000以内的素数
    # for n in primes():
    #     if n < 1000:
    #         print(n)
    #     else:
    #         break
    output = filter(is_palindrome, range(1, 1000))
    print(list(output))


if __name__ == '__main__':
    main()

# filter返回的是一个Iterator,惰性序列，所以要强迫filter()完成计算结果，需要用list（）函数获得所有结果并返回list
