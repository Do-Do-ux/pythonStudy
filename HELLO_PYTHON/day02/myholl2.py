from random import random

mine = input("홀/짝을 선택하시오")

num = random()
com = 0;
me = 0;
result = ""
print(num)
if num > 0.5:
    com = 1
else:
    com = 0

if mine == "홀":
    me = 1
else:
    me = 0

if me == com:
    result = "이김"
else:
    result = "짐"

if com == 1:
    com ="홀"
else:
    com = "짝"
print("컴:",com)
print("나:",mine)
print("결과:",result)