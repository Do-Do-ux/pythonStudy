# 첫수를 입력하세요 3
# 끝수를 입력하세요 5

#★★★
#★★★★
#★★★★★

def star(cnt):
    for i in range(cnt):
        print("*",end="")
    print()
        
a = input("첫수를 입력하세요")
b = input("끝수를 입력하세요")

aa = int(a)
bb = int(b)

for i in range(aa,bb+1):
    star(i)
    
        
        