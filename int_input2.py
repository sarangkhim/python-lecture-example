import re


def input_int():
    msg = input()
    m = re.sub(r'and', ' ', msg)

    return [int(n) for n in input(m).split()]

if __name__ == "__main__":
    n = input_int()

    for i in n:
        print(i, end=' ')
