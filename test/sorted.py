def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


def main():
    print(sorted([36, 5, -12, 9, -21], key = abs))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)
    print(L2)
    L3 = sorted(L, key=by_score, reverse=True)
    print(L3)

if __name__ == '__main__':
    main()
