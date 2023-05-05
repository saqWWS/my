import string


def alphabet():
    alphabet = list(string.ascii_lowercase)
    return alphabet


def decode():
    key = int(input("num:\t"))
    text = input("encode:\t").lower()
    str_ = ""
    alpha = alphabet()
    for i in range(len(text)):
        index_of_alpha = alpha.index(text[i])
        print("Տառի ինդեքս", index_of_alpha)
        print("Այն ինդեքսը, որը ստացվել է", index_of_alpha + key)
        if index_of_alpha + key > len(alpha):
            print(alpha[len(alpha) - index_of_alpha - 1])
        else:
            str_ += alpha[index_of_alpha + key]
        print(str_)


print(decode())
