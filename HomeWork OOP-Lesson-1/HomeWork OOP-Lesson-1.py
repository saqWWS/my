# class Rectangle:
#     lenght = int(input("Number on your mind:\t"))
#     width = int(input("What's on your mind:\t"))
#
#     def area(self, lenght, width):
#         return lenght * width
#
#     def perimeter(self, lenght, width):
#         return 2 * lenght + width
#
#
# rectangle = Rectangle()
# rectangle.area()
# print(rectangle.area(), rectangle.perimeter())
# Rectangle = rectangle.lenght, rectangle.width
# Էս որ քնարկենք, ինչու է այդպես))


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
#
# rectangle = Rectangle(lenght=int(input("Number on your mind:\t")), width=int(input("What's on your mind:\t")))
# print("Մակերես:", rectangle.area())
# print("Պարագիծ:", rectangle.perimeter())
# N1




# import random
#
#
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self):
#         account_number_ = 553612
#         self.account_number = int(input("Մուտքագրեք ձեր հաշվեհամարը։\t"))
#         if self.account_number == account_number_:
#             print("Ձեր հաշվի մնացորդը կազմում է:\t", self.balance)
#             amount = float(input("Մուտքագրեք գումարի չափը:\t"))
#             self.balance += amount
#             print("Ձեր ընդանհուր գումարը կազմում է:", amount and self.balance)
#         else:
#             print("Որևէ բան սխալ է: \n Խնդրում ենք փորձել ավելի ուշ. \n Շնորհակալություն!")
#
#     def withdraw(self):
#         account_number_ = 553612
#         self.account_number = int(input("Մուտքագրեք ձեր հաշվեհամարը։\t"))
#         if self.account_number == account_number_:
#             print("Ձեր հաշվի մնացորդը կազմում է:\t", self.balance)
#             amount = float(input("Ելքագրել գումարի չափը:\t"))
#             if self.balance <= amount:
#                 print("\n Ձեր հաշվին չկա բավարար միջոցներ.\n Շնորհակալություն!")
#             else:
#                 self.balance -= amount
#                 print("Ձեր ընդանհուր գումարը կազմում է:\t", amount and self.balance)
#         else:
#             print("\n Որևէ բան սխալ է:\n Խնդրում ենք փորձել ավելի ուշ.\n Շնորհակալություն!")
#
#
# account_number = 553612
# balance = random.randint(1, 5000)
# selfaccount = BankAccount(account_number, balance)
#
# if account_number == 553612:
#     press = int(input("Մուտքագրման համար սեղմեք.\t" + "1\n"
#                        "Ելքագրման համար սեղմեք.\t" + "2\n"
#                        "Հաշվի մնացորդը տեսնելու համար սեղմեք․\t" + "3\n" + "Click:\t"))
#     if press == 1:
#         selfaccount.deposit()
#     elif press == 2:
#         selfaccount.withdraw()
#     elif press == 3:
#         print("Հաշվի մնացորդ:\t", selfaccount.balance)
#     else:
#         print(print("\n Որևէ բան սխալ է:\n Խնդրում ենք փորձել ավելի ուշ.\n Շնորհակալություն!"))
#
# N2


