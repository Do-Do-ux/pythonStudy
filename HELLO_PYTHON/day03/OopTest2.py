class Vehicle:
    def __init__(self):
        self.cnt_wheel = 4
        
    def platTire(self):
        self.cnt_wheel -= 1
        

tire = Vehicle();
print(tire.cnt_wheel)        
tire.platTire();
print(tire.cnt_wheel)        