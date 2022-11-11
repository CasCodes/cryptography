from english_words import english_words_set
import re

# get input
def get_input():
    text = input('enter text: ').lower()
    key = int(input('enter key: '))
    return text, key

def caesar(text: str, key: int, mode: int) -> str:
    key = -key if mode == 1 else key
    cipher = ""
    for i in text:
        # handle spaces and other weird characters
        if 126 >= ord(i) >= 33 :
            # handle out of bounds increase with mod
            cipher += chr((ord(i) + key - 33) % 93 + 33)
        else:
            cipher += i
    return cipher



t, k = get_input()
e = caesar(t, k, 0)
f = caesar(e, k, 1)
print(e,'\n', f)