sum = 0
for i in range(11, 100):
    if i % 4 == 1:
        sum += i
        print(i)
print("Բոլոր թվերի գումարը", sum)

N1


t = int(input("եղանակի տեսություն:\t"))
if t <= 18:
    print("Հաճելի է")
elif 18 < t < 24:
    print("Շոգ է!")
elif t >= 24:
    print("Այստեղ անհնար է!")
N2


num = 0
while num < 40:
    print("Num", num)
    num += 1
N 3.1

for i in range(7, 30):
    if i % 2 == 0:
        print("Num", i)
N3.2

for x in range(100, 600):
    if (x % 3 == 0) and (x % 11 == 0) and (x % 7 != 0):
        if x == 231 or x == 462:
            continue
        print(x)
N4


start = int(input("First number:\t"))
end = int(input("Second number:\t"))
for i in range(start, end):
    if i % 7 == 0:
        print(i)
N5
