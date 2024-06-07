# # 첫수를 입력하시오 1
# # 끝수를 입력하시오 10
# # 배수를 입력하시오 3
#
# # 1에서 10까지의 3의 배수의 합은 18입니다.

a = input("첫 수를 입력하시오")
b = input("끝 수를 입력하시오")
c = input("배수를 입력하시오")

aa = int(a)
bb = int(b)
cc = int(c)

sum = 0

for i in range(aa,bb+1):
    if i % cc == 0:
        print(i)
        sum += i
        
print("{}에서 {} 까지의 {}의배수의 합은 {} 입니다.".format(aa,bb,cc,sum))


        