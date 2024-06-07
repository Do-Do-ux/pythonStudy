a = input("첫 수를 입력 하시오")
b = input("끝 수를 입력 하시오")

sum = 0

aa = int(a)
bb = int(b)

for i in range(aa,bb+1):
    sum += i
print("{} 에서 {} 까지의 합은 {} 입니다.".format(a,b,sum))