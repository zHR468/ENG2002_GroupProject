from fixnum_module import fixNum


def test():
    a = fixNum(12, 48)
    b = fixNum(2, 16)
    print(a)
    print(b)
    c = fixNum(0, 21)
    print(c)
    d = fixNum(0, 0)
    print(d)


if __name__ == "__main__":
    test()
