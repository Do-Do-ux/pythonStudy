a = int(input("첫수를 입력하시오"))
b = int(input("끝수를 입력하시오"))

if a > b :
    print("{}는 {}보다 크다".format(a,b))
elif b > a:
    print("{}는 {}보다 작다".format(a,b))
else:
    print("두 수는 같다")
    