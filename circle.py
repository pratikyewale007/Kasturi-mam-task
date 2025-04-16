class Circle:
    pi = 3.14
    
    def _init_(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def radius(self):
        self.Radius = float(input('Enter a radius of circle : '))
    
    def Area(self):
        self.Area = Circle.pi * self.Radius
    
    def Circumeference(self):
        self.Circumference = 2 * Circle.pi * self.Radius
    
    def Display(self):
        print(f'Radius of circle: {self.Radius} \nArea Of Circle : {self.Area} \nCircumference Of Circle: {self.Circumference} ')

def main():
    circle1 = Circle()
    
    circle1.radius()
    circle1.Area()
    circle1.Circumeference()
    
    circle1.Display()
        
if __name__ == '__main__':
    main()