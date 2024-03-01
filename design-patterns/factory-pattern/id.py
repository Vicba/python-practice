
class A():
    pass


if __name__ == '__main__':
    a = A()
    b = A()

    # conclusion: a and b are different objects
    print(a == b)
    print(id(a) == id(b))
    print(a, b)