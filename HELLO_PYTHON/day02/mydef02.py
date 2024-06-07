from random import random
def getHJ():
    num = 0;
    num = random()
    if num > 0.5:
        com = "홀"
    else:
        com = "짝"
    return com

com = getHJ()
print("com",com)