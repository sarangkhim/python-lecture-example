def obj():
    a = 5
    pass


def boo():
    print("Hello")

obj.a = 10
obj.b = boo

print(obj.a)
obj.b()

obj()