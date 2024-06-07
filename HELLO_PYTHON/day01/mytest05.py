#출력 단수를 입력하시오
# 7 * 1 = 7

a = input("출력 단 수를 입력 하시오")
aa = int(a)
for i in range(1,9+1):
    print("{} * {} = {}".format(aa,i,aa*i))
