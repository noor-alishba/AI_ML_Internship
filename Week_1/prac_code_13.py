# Shape Area Calculator (Polymorphism)


class Shape:

    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.l*self.w

class Circle(Shape):

    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*self.r*self.r

shapes=[Rectangle(5,4),Circle(3)]

for shape in shapes:
    print(shape.area())