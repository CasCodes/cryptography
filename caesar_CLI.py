
from english_words import english_words_set
import re

mode = int(input('(0) Encrypt (1) Decrypt (2) Hack: '))

# get input
def get_input():
    text = input('enter text: ')
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

# super secret mode pssst
def hack() -> str:
    text = input("text2hack: ")
    # split at spaces, ignoring special chars  zruog khoor$ -> world hello!
    words = text.lower().split()
    for word in words:
        # brute force every key
        for i in range(93):
            temp = caesar(word, i, 1)
            # check if a known word is found
            if temp in english_words_set:
                print('Hacked! Key = ', i)
                return caesar(text, i, 1)
    return 'Super secret hacker failed!'

if mode == 0:
    t, k = get_input()
    print(caesar(t, k, 0))
elif mode == 1:
    t, k = get_input()
    print(caesar(t, k, 1))
elif mode == 2:
    print(hack())
else:
    print('please select a valid mode')
    