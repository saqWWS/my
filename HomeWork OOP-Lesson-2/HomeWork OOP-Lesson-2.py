#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         return self.name, self.age
#
#
# class Student(Person):
#     def __init__(self, name, age, section):
#         Person.__init__(self, name, age)
#         self.section = section
#
#     def displayStudent(self):
#         return self.section
#
#
# student = Student("Ioana", "24", "Programmer")
# student.age = 24
# print(student.name, student.age, student.section)

# N1



# class Rectangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#
#     def area(self):
#         return self.lenght * self.width
#
#     def perimeter(self):
#         return 2 * (self.lenght + self.width)
#
#     def disply(self):
#         return self.lenght, self.width, self.area(), self.perimeter()
#
#
# class Parallelepipede(Rectangle):
#     def __init__(self, lenght, width, height):
#         Rectangle.__init__(self, lenght, width)
#         self.height = height
#
#     def volume(self):
#         return self.lenght * self.width * self.height
#
#     def lewihe(self):
#         return self.lenght, self.width, self.height
#
#
# rectangle = Rectangle(lenght=int(input("Number on your mind:\t")), width=int(input("What's on your mind:\t")))
# parallelepipede = Parallelepipede(lenght=int(input("Number on your mind:\t")),
#                                   width=int(input("What's on your mind:\t")),
#                                   height=int(input("Whatever you want\t")))
# print("Մակերես:", rectangle.area())
# print("Պարագիծ:", rectangle.perimeter())
# print("Բոլորը միասին:\t", rectangle.disply())
# print("Զուգահեռանիստ:\t", parallelepipede.volume())
# print("Զուգահեռանիստի թվերը:\t", parallelepipede.lewihe())

# N2