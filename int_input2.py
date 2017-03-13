import re


#def input_int():
#    msg = input()
#    m = re.sub(r'and', ' ', msg)
#
#    return [int(n) for n in input(m).split()]

def input_int(msg=''):
    p = re.compile(r'\d+[.0-9]*')
    return map(int, p.findall(input(msg)))

if __name__ == "__main__":
    ret = input_int()

    for i in ret:
        print(i, end=' ')
