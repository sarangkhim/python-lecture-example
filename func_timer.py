import time


def add_for(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


def add_while(n):
    total = 0
    while n:
        total += n
        n -= 1
    return total


def add_gauss(n):
    total = round((1+n) * (n/2))
    return total


def perf_count(func, n):
    t0 = time.perf_counter()
    ret = func(n)
    t1 = time.perf_counter()
    print("[%-10s] %.20f seconds" % (func.__name__, t1-t0))


def main():
    n = 10000000

    perf_count(add_for, n)
    perf_count(add_while, n)
    perf_count(add_gauss, n)


if __name__ == "__main__":
    main()
