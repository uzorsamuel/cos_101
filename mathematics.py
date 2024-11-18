print('welcome to mathematics class')

def area_of_triangle():
    base=int(input('Enter the base of the triangle: '))
    height=int(input('Enter the height of the triangle: '))
    area=0.5 * base * height
    print(area)

def area_of_square():
    length=int(input('Enter the length of the square: '))
    area= length ** 2
    print(area)

def area_of_rectangle():
    length=int(input('Enter the length of the rectangle: '))
    width=int(input('Enter the width of the rectangle: '))
    area=length * width
    print(area)

def area_of_trapezoid():
    base1=int(input('Enter the first base of the trapezoid: '))
    base2=int(input('Enter the second base of the trapezoid: '))
    height=int(input('Enter the height of the trapezoid: '))
    area=(base1+base2) * height/2
    print(area)

def area_of_parallelogram():
    base=int(input('Enter the base of the parallelogram: '))
    height=int(input('Enter the height of the parallelogram: '))
    area=base*height
    print(area)


def calculate_area():
    print('what will you like to learn?')
    print('(A)Area of triangle')
    print('(B)Area of square')
    print('(C)Area of rectangle')
    print('(D)Area of trapezoid')
    print('(E)Area of parallelogram')

    choice=input('select a letter:')

    if choice == 'A' or choice == 'a':
        area_of_triangle()
    elif choice == 'B' or choice == 'b':
        area_of_square()
    elif choice == 'C' or choice == 'c':
        area_of_rectangle()
    elif choice == 'D' or choice == 'd':
        area_of_trapezoid()
    elif choice == 'E' or choice == 'e':
        area_of_parallelogram()
    else:
        print('invalid selection, please select an alphabet between A - E.')

calculate_area()