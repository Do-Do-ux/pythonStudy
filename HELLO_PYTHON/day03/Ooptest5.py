class LeeSS:
    def __init__(self):
        self.cnt_turtleship = 12;
    
    def battle(self):
        self.cnt_turtleship-=1
        
class LeeJY:
    def __init__(self):
        self.stock = 1000000;
    
    def yakun(self,cnt):
        self.stock += cnt

class Elon:
    def __init__(self):
        self.bitcoin = 10000;
    
    def business(self):
        self.bitcoin-=1

        
class Im(LeeJY,LeeSS,Elon):
    def __init__(self):
        
        LeeSS.__init__(self) 
        LeeJY.__init__(self) 
        Elon.__init__(self) 
        
i = Im()
print(i.cnt_turtleship)
print(i.stock)
print(i.bitcoin)
i.battle()
i.yakun(30)
i.business()
print(i.cnt_turtleship)
print(i.stock)
print(i.bitcoin)

        
        
        

        
    