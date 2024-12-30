class Circle():
    #Class Attribute
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    def circumference(self):
        return 2 * Circle.pi * self.radius
    
mycircle = Circle(radius=9)

print(f'Area of circle [ radius => {mycircle.radius} ] : {mycircle.area:0.2f}')
print(f'Circumference of circle [ radius => {mycircle.radius} ] => {mycircle.circumference():0.2f}')