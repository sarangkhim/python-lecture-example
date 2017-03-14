import re


def input_fmt(fm, msg=''):
    ptn = ''
    conv = []

    for c in fm:
        if c == 'i':  # r'(\d+)'
            ptn += r'(\d+)'
            conv.append(int)
        if c == 'f':  # r'([\d+.])'
            ptn += r'([\d+.])'
            conv.append(float)
        if c == 'b' or c == 's':  # r'(\w+)'
            ptn += r'(\w+)'
            conv.append(str)

    print(conv)

    m = input(msg)
    pt = re.compile(ptn)

    return pt.search(m)


if __name__ == "__main__":
    ret = input_fmt('iibsf', 'enter num: ')

    for i in ret:
        print(i, end=' ')
