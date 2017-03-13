print("안녕! 내 이름은 보미야~")
you = input("이름이 뭐니? ")

print("네 이름은 %s이 구나~" % you)

try:
    n = int(input())
    print(3/n)
except ValueError as e:
    print(e)
