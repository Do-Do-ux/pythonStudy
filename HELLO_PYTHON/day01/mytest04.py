# 수를 입력 하시오 5 6
# 5는 짝수가 아닙니다.
# 6은 짝수 입니다.

a = input("수를 입력 하시오")

aa = int(a)
if aa % 2 == 0 :
    print("{} 는 짝수 입니다".format(a))
else :
    print("{} 짝수가 아닙니다.".format(a))