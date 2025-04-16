class Number:
    def _init_(self):
        self.value1 = 0
        self.value2 = 0
        
    def Accept(self):
        self.value1 = int(input('Enter 1st NO.: '))
        self.value2 = int(input('Enter 2nd No.: '))
    
    def Addition(self):
        return self.value1 + self.value2
     
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        if self.value2 !=0:
            return self.value1  / self.value2
        else:
            return 'Division by zero is not allowed'
    
def main():
    num = Number()
    num.Accept()
    print('Addition: ', num.Addition())
    print('Subtraction: ', num.Subtraction())
    print('Multiplication: ', num.Multiplication())
    print('Division: ', num.Division())
    
if __name__ == '__main__':
    main()