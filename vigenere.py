"""

██╗░░░██╗██╗░██████╗░███████╗███╗░░██╗███████╗██████╗░███████╗
██║░░░██║██║██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔════╝
╚██╗░██╔╝██║██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝█████╗░░
░╚████╔╝░██║██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══╝░░
░░╚██╔╝░░██║╚██████╔╝███████╗██║░╚███║███████╗██║░░██║███████╗
░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚══════╝
"""

# get input
def get_input():
    mode =  int(input('(0) Encrypt (1) Decrypt: '))
    text = input('enter text: ').upper()
    keyword = input('enter keyword: ').upper()
    return text, keyword, mode

# repeat the key for the lenght of the text
def generate_key(text, keyword):
    return (keyword * (len(text)//len(keyword) + 1))[:len(text)]

# encrypt text with key
def encrypt(text, key):
    cipher = []
    for i in range(len(text)):
        if text[i].isalpha():
            c = (ord(text[i]) + ord(key[i])) % 26
            c += ord('A')
            cipher.append(chr(c))
        else:
            cipher.append(text[i])
    return "".join(cipher)

# decrypt text with key
def decrypt(text, key):
    plain = []
    for i in range(len(text)):
        if text[i].isalpha():
            c = (ord(text[i]) - ord(key[i]) + 26) % 26
            c += ord('A')
            plain.append(chr(c))
        else:
            plain.append(text[i])
    return "".join(plain)

text, key_word, mode = get_input()
key = generate_key(text, key_word)

if mode == 0:
    cipher = encrypt(text, key)
    print(cipher)
elif mode == 1:
    plain = decrypt(text, key)
    print(plain)
else:
    print("please select a mode")