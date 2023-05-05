english = {
    "Variable": "Փոփոխական",
    "Declaration": "Հայտարարում",
    "Assignment": "Վերագրում",
    "Data types": "Տվյալների տիպեր",
    "Integer": "Թվյաին տիպ",
    "String": "Տողային տիպ",
    "Boolean": "Բուլյան տիպ",
    "true": "Ճշմարիտ",
    "Else": "Հակառակ դեպքում",
    "Array": "Զանգված",
    "If": "Եթե",
    "False": "Կեղծ"

}
dictionary = input("Write and see:\t")
for word in english.keys():
    if word.upper() == dictionary.upper():
        print(english[word])
else:
    print("Wrong text, try again")
