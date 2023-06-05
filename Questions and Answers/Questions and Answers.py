# input = int(input("Enter the number of rows:\t"))
# for i in range(1, input):
#     for x in range(1, i + 1):
#         print(x, end="")
#     print()
# # ԽՆԴԻՐ 1
#
#
# thenumbers = [12, 75, 150, 180, 145, 525, 50]
# for i in thenumbers:
#     if i == 500:
#         break
#     elif i >= 150:
#         continue
#     elif i % 5 == 0:
#         print(i)
# # ԽՆԴԻՐ 2
#
#
# number = input("the number:\t")
# print(len(number))
# # ԽՆԴԻՐ 3.1
#
#
# num = int(input("Your mind:\t"))
# count = 0
#
# while num != 0:
#     num //= 10
#     count += 1
#
# print("Թվերի քանակը։ " + str(count))
# # ԽՆԴԻՐ 3․2
#
#
# first = int(input("Number:\t"))
# second = int(input("Number:\t"))
# LList = []
# for num in range(first, second):
#     if num > 1:
#         if num % 2 == 0:
#             continue
#         for x in range(3, (num//2)+1):
#             if num % x == 0:
#                 break
#         else:
#             LList.append(num)
# print(LList)
# # ԽՆԴԻՐ 4
#
#
# Input = int(input("Write your number:\t"))
# put = int(input("Write your number:\t"))
# for i in range(0, Input):
#     for x in range(0, i + 1):
#         print("*", end=" ")
#     print()
#
# for l in range(put, 0, - 1):
#     for k in range(0, l - 1):
#         print("*", end=" ")
#     print()
# # խՆԴԻՐ 5
#
#
# input = int(input("Write your number:\t"))
# for i in range(0, input):
#     for x in range(0, i + 1):
#         print("*", end=' ')
#     print()
# # ԽՆԴԻՐ 5․1
#
#
# put = int(input("Write your number:\t"))
# for l in range(put, 0, - 1):
#     for k in range(0, l - 1):
#         print("*", end=" ")
#     print()
# # խՆԴԻՐ 5․2
#
# _dict = {
#     "Car": "Alfa Romeo",
#     "Model": "Giulia",
#     "Year": "2021",
#     "Model_type": "Quadrifoglio",
#     "Color": "Dark Blue",
#     "Engine": "2.9",
#     "Engine_type": "Turbo",
#     "Horse_Power": "512",
#     "Manufacturer": "Italy"
# }
#
# result = {}
# for value in _dict.values():
#     result[value] = len(value)
#
# print(result)
#
# # ԽՆԴԻՐ 6
#
#
# _words = input("Word:\t").lower().split()
# print(_words)
# word_count = {}
# for word in _words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)
# for key, value in word_count.items():
#     print(f"Բառ: {key}, Քանակ: {value}")
# # ԽՆԴԻՐ 7
#
#
# number = int(input("Write the number:\t"))
# sum = 0
# for i in range(1, number):
#     if number % i == 0:
#         sum = sum + i
# if sum == number:
#     print("Կատարյալ է։")
# else:
#     print("Կատարյալ չէ։")
# # ԽՆԴԻՐ 8
#
#
# import random
#
# _list = []
# negatives = []
# positives = []
# for i in range(20):
#     _list.append(random.randint(-100, 100))
# print("Բոլոր թվերը:\t", _list)
#
# for number in _list:
#     if number < 0:
#         negatives.append(number)
#     else:
#         positives.append(number)
#
# print(f"Դրական թվեր:\t", positives, "Դրական թվերի քանակը։", len(positives))
# print("Բացասական թվեր:\t", negatives, "Բացասական թվերի քանակը։", len(negatives))
# ԽՆԴԻՐ 9
#
#
# import random
#
# all_number = []
# for i in range(10):
#     random_list = random.randint(1, 32)
#     all_number.append(random_list)
# print("Original list:", all_number)
# first = int(input("First index:\t"))
# second = int(input("Second index:\t"))
# all_number[first], all_number[second] = all_number[second], all_number[first]
# print("Changed list:", all_number)
# # խնդիր 10