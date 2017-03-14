import math

data = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
carry = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i, n in enumerate(data):
    #carry[i] = round(n)
    carry[i] = math.ceil(n)

ret_zip = zip(data, carry)   
for d1, d2 in ret_zip:
    print("{} --> {}".format(d1, d2))

target = "1300 * 0.175" 
print("{} = {}".format(target, round(eval(target))))
