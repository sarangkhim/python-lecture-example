def input_int(msg):
    if True:
        return [int(i) for i in input(msg).split()]
    else:
        return map(int, input().split())

if __name__ == "__main__":
    n = input_int()

    for i in n:
        print(i, end=' ')
