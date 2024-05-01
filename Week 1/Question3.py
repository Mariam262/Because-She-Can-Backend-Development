
"""Question3
3. Write a python code that calculates and
displays the perimeter and area of;
a. Square; given that the length of one
side is 8cm
b. Rectangle; given that the length and
width of the rectangle are 4cm and
6cm respectively."""


class Shape:
    def calc_sqrarea(self,length):
        area=length*length
        print("Area of square:", area)

    def calc_sqrperi(self, length):
        perim =  4 * length
        print("Perimeter of square:", perim)

    def calc_recarea(self,length,width):
        area=length*width
        print("Area of rectangle:", area)

    def calc_recperi(self,length,width):
        perim = 2 * (length + width)
        print("Perimeter of rectangle:", perim)


myshape=Shape()
myshape.calc_sqrarea(8)
myshape.calc_sqrperi(8)
myshape.calc_recarea(4,6)
myshape.calc_recperi(4,6)


