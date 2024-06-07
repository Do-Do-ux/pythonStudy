class Drink:
    def __init__(self):
        self.mg = 200
        print("생성자")
    def one_plus_one(self):
        self.mg = 400
        
    def __del__(self):
        print("소멸자")
        
    def __str__(self):
        return "밀리그램:"+str(self.mg) #JAVA에 toString과 똑같은 느낌
        
dk = Drink()
print(dk)
dk.one_plus_one()
print(dk)
    
        