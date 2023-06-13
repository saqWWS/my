def perimetr_of_rectangle_and_area(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area


_length = float(input("Երկարություն։\t"))
_width = float(input("Լայնությունը:\t"))

print(perimetr_of_rectangle_and_area(_length, _width))


# N1 and N3
#
#


def perimeter_of_square_and_area(square):
    area = square * square
    perimeter = 4 * square
    print("Տարածք:", area)
    print("Պարագիծ:", perimeter)


local = int(input("Write:\t"))
perimeter_of_square_and_area(local)
# N2 and N4
