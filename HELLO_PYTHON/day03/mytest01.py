# 가위/바위/보 를 입력하세요 가위
# 나:가위
# 컴:가위
# 결과: 비김
from random import  randint

human = input("가위/바위/보 를 입력하세요: ")
gawi = ["가위","바위","보"]
a = randint(0,2)
com = gawi[a]

result = "이김"
if com == "가위"  and human == "보":
    result = "짐"
elif com == "바위" and human == "가위":
    result = "짐"
elif com == "보" and human == "바위":
    result = "짐"
elif com == human :
    result = "비김"
else:
    result = "이김"
    
print("나 : {} \n컴 : {} \n결과 : {}".format(human,com,result))
     
