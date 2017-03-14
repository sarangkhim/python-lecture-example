import doctest


def my_func(n):
    """
    >>> my_func(10)
    55
    >>> my_func(100)
    505
    """
    s = 0
    for n in range(n+1):
       s += n
    print(s)

if __name__ == "__main__":
    doctest.testmod()
