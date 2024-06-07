class Animal:
    """ Super Class """
    def __init__(self):
        self.flag_gen = True
    
    def goToThai(self):
        self.flag_gen = not self.flag_gen

if __name__ == '__main__':
    ani = Animal()
    print("뭐고 씨",ani.flag_gen)
    ani.goToThai()
    print("뭐고 씨",ani.flag_gen)
        