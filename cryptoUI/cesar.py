from english_words import english_words_set
import re

"""
cesaer cipher (encrypt, decrypt and hack)
"""

def encrypt_cesar(text, key) -> str:
    text = text.lower()
    cipher = ""
    for i in range(len(text)):
        # check for alphabetic characters
        if text[i].isalpha():
            # substract ascii value of char by key
            # account for values < a
            val = ord(text[i])
            if val - key < 97:
                # alphabetical position of char (starting at 1)
                cipher += chr((val - key) + 26)
            else:
                cipher += chr(ord(text[i])-key)
        else:
            cipher += text[i]
    return cipher

def decrypt_cesar(text, key) -> str:
    plain = ""
    for i in range(len(text)):
        if text[i].isalpha():
            # add key to ascii value of char
            val = ord(text[i])
            if val+key > 122:
                plain += chr((val + key) - 26)
            else:
                plain += chr(ord(text[i])+key)
        else:
            plain += text[i]
    return plain

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