from random import random

gawi = random()
print(gawi)
com = ""

if gawi > 0.66:
    com = "가위"
elif gawi > 0.33:
    com = "바위"
else: 
    com = "보"
    
print(com)
