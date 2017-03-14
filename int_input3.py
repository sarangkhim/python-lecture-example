import re


def input_fmt(fm, msg=''):
    ptn = r''
    conv = []

    for c in fm:
        if c == 'i':  # r'(\d+) '
            ptn += r'(\d+) '
            conv.append(int)
        if c == 'f':  # r'([\d+.]) '
            ptn += r'([\d+.]) '
            conv.append(float)
        if c == 'b' or c == 's':  # r'(\w+) '
            ptn += r'(\w+) '
            conv.append(str)

    ptn.rstrip()
    data = input(msg)
    return [t(s) for t, s in zip(conv, re.search(ptn, data).groups())]


if __name__ == "__main__":
    ret = input_fmt('iif', 'enter num: ')

    for i in ret:
        print(i, end=' ')
