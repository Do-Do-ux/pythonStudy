#up and down 게임
#random을 이용해서 1~99
#맞출수를 입력하세요
#10 up!
#맞출 수를 입력하세요 60 down!
#맞추면 50 정답입니다.
from random import  randint

com = int(randint(1,99+1))


while True:
    a = input("맞출수를 입력하세요")
    human = int(a)
    if com > human:
        print("{} up!".format(human))
    elif com < human:
        print("{} down!".format(human))
    elif com == human:
        print("{} 정답입니다.".format(human))
        break
        