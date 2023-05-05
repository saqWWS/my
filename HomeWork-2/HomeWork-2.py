_evodd = int(input("Check the number:\t"))
if _evodd % 2 == 0:
    print("even")
    if _evodd % 3 == 0:
        print("Բաժանվում է և՛ երկուսի, և՛ երեքի:")
else:
    print("odd")




_input = int(input("Input:\t"))
__input = int(input("input:\t"))
if _input == __input:
    print("All numbers are equal")
else:
    print(max(_input, __input))


a = 15
b = 97
if a == b:
    print(a)
elif a > b:
    print("A is greater than b")
else:
    print("B is greater than A")




number = int(input("the number:\t"))
if number % 5 == 0 and number % 7 == 0:
    print("Բաժանվում է 5 ու 7-ի։")
elif number % 5 == 0:
    print("Բածանվում է 5-ի:")
elif number % 7 == 0:
    print("Բաժանվում 7-ի:")
else:
    print("Չի բաժանվում:")
