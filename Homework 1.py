# Створіть клас Rectangle для представлення прямокутника.
# Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи.

class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area (self, h, w):
        rectangle_area = self.h * self.w
        print(f"Rectangle area is {rectangle_area} ")

    def pergmeter(self, h, w):
        rectangle_pergmeter = (self.h + self.w) * 2
        print(f"Rectangle pergmeter is {rectangle_pergmeter} ")

h = int(input("Enter rectangle height: "))
w = int(input("Enter rectangle width: "))

retangle = Rectangle(h, w)
retangle.area(h, w)
retangle.pergmeter(h, w)
