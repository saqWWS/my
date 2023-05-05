def my_creation():
    f = open("creation", "r")
    print(f.read())


my_creation()

# homework - 1

def new_line():
    f = open("creation", 'r')
    s = f.read()
    x = s.split()
    print(str(len(x)) + " " + "Words")


new_line()
# homework - 2.0


def line():
  f = open("creation.txt", "w")
  f.write(input("Write:\t"))
  f = open("creation.txt", "r")
  mylist = list(f)
  print(f.read(), mylist)
  f.close()

line()
# homework - 3


def read_data():
    f = open("creation", "r")
    read = f.read().split()
    for i in read:
        if len(i) <= 4:
            print(i)


read_data()
# homework - 4
# Էս ոչ մի ձե չեղավ, երևի մի հատ բացատրեք, հասկանամ որտեղ է խնդիրը, համենայնդեպս ուղարկում եմ:


f_1 = open("creation", "r")
f_2 = open("creation.txt", "w")
for line in f_1:
    f_2.write(line)
f_2 = open("creation.txt", "r")
print(f_2.read())
# homework - 5