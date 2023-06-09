import string


def alphabet():
    alphabet = list(string.ascii_lowercase)
    return alphabet


def encode(key, text):
    str_ = ""
    alpha = alphabet()
    for i in range(len(text)):
        print(i)
        index_of_alpha = alpha.index(text[i])
        print("Տառի ինդեքս:", index_of_alpha)
        print("Այն ինդեքսը, որը ստացվել է:", index_of_alpha + key)
        if index_of_alpha + key > len(alpha):
            print(alpha[len(alpha) - index_of_alpha - 1])
        else:
            str_ += alpha[index_of_alpha + key]
        print(str_)
    return str_


_key = int(input("Please write the number:\t"))
_text = input("You can only write text:\t").lower()
print(encode(_key, _text))


def decode(key, text):
    str_ = ""
    alpha = alphabet()
    for i in range(len(text)):
        print(i)
        index_of_alpha = alpha.index(text[i])
        print("Տառի ինդեքս:", index_of_alpha)
        print("Այն ինդեքսը, որը ստացվել է:", index_of_alpha - key)
        if index_of_alpha + key > len(alpha):
            print(alpha[len(alpha) - index_of_alpha - 1])
        else:
            str_ += alpha[index_of_alpha - key]
        print(str_)
    return str_


_key = int(input("Please write the number:\t"))
_text = input("You can only write text:\t").lower()
print(decode(_key, _text))
