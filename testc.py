from english_words import english_words_set
import re

# get input
def get_input():
    text = input('enter text: ').lower()
    key = int(input('enter key: '))
    return text, key

def encrypt(text, key):
    cipher = ""

    for i in text:
        # catch values out of bound
        if (ord(i) + key) > 126:
            # cap between ascii value 33 & 126
            val = ord(i) + key % (126 - 32)
            if val > 126:
                val = val % 126 + 32
            cipher += chr(val)
        else:
            cipher += chr(ord(i) + key)
    
    print(cipher)
    return cipher

def decrypt(text, key):
    cipher = ""
    # khoor/#zruog$
    for i in text:
        # catch values out of bound
        if (ord(i) - key - 33) < 33:
            # cap between ascii value 33 & 126
            val = ord(i) - key - 32
            val = 126 + val
            cipher += chr(val)
        else:
            cipher += chr(ord(i) - key)
    
    print(cipher)

t, k = get_input()
e = encrypt(t, k)
decrypt(e, k)