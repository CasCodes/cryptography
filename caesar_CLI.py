
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

# super secret mode 
def hack() -> str:
    text = input("text2hack: ").lower()
    # split at spaces, ignoring special chars
    words = re.sub(r'[,\.!?]', '', text).split()
    for word in words:
        temp = list(word)
        for i in range(26):
            for j in range(len(word)):
                if temp[j].isalpha():
                    val = ord(word[j])
                    if val+i > 122:
                        temp[j] = chr((val+i) - 26)
                    else:
                        temp[j] = chr(val+i)
            if "".join(temp) in english_words_set:
                # if cracked & multiple words, decipher entire input
                if len(words) > 1:
                    t = ""
                    for k in list(text):
                        t += chr(ord(k)+i) if k.isalpha() else k
                else:
                    t = "".join(temp)
                return(f"hacked!\n key = {i}\n text = {t}")
    return("super secret hacker failed")


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
    