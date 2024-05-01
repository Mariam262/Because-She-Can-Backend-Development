"""Question3
3. Write a python code that calculates and
displays the perimeter and area of;
a. Square; given that the length of one
side is 8cm
b. Rectangle; given that the length and
width of the rectangle are 4cm and
6cm respectively. with functions """


def calc_sqrinfo(length):
    area = length * length
    print("Area of square:", area)
    perim = 4 * length
    print("Perimeter of square:", perim)


def calc_recinfo(length, width):
    perim = 2 * (length + width)
    print("Perimeter of rectangle:", perim)
    area = length * width
    print("Area of rectangle:", area)




def main():
    length_sqr=8       #square
    calc_sqrinfo(length_sqr)

    length_rec = 4
    width_rec = 6
    calc_recinfo(length_rec,width_rec)


if __name__ == "__main__":
        main()