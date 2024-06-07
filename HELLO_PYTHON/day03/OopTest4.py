from day03.OopTest import Animal

class Human(Animal):
    """ Child Class """
    def __init__(self):
        super().__init__()
        self.skill_communication = 1
        
    def momstouch(self,stroke):
        self.skill_communication += stroke;
    
if __name__ == '__main__':
    hu = Human();
    print("an.flag_gen",hu.flag_gen)
    print("hu.momstouch",hu.skill_communication)
    hu.goToThai()
    hu.momstouch(5)
    print("an.flag_gen",hu.flag_gen)
    print("hu.momstouch",hu.skill_communication)
    