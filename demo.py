class Demo:
    val = 0
    def _init_(self, value1, value2):
        self.val1 = value1
        self.val2 = value2
    
    def Fun(self):
        print(f'Fun: \n value1 = {self.val1} \n value2 = {self.val2}')
        
    def Gun(self):
        print(f'Gun: \n value1 = {self.val1} \n value2 = {self.val2}')

def main():
    Obj1 =Demo(11,21)
    Obj2 = Demo(51,101)
    
    Obj1.Fun()
    Obj2.Fun()
    print('')
    Obj1.Gun()
    Obj2.Gun()

if __name__ == '__main__':
    main()  