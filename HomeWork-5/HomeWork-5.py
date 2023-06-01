mainlist = int(input("Numbers\t"))
_list = []
for i in range(mainlist):
    s = int(input("Input ...\t"))
    _list.append(s ** 2)
print(_list)
# N1

mainlist = int(input("Numbers\t"))
_list = []
sum = 0
for i in range(mainlist):
    secondinput = int(input("Input ...\t"))
    _list.append(secondinput)
for io in (_list):
    sum += io
print(_list)
print(sum)
# N2


mainlist = int(input("Numbers\t"))
_list = []
sum = 1
for i in range(mainlist):
    secondinput = int(input("Input ...\t"))
    _list.append(secondinput)
for io in (_list):
    sum *= io
print(_list)
print(sum)
# N3


numberslist = int(input("How many numbers do you want to generate?\t" + "\n"))
lisT = []
for num in range(numberslist):
    numbers = int(input("Write in order in order:\t"))
    lisT.append(numbers)
for i in range(len(lisT)):
    if lisT[i] == 20:
        lisT[i] = 200
        break
else:
    print("Number 20 is not in that list, try again:\t")
print(lisT)

# N4
