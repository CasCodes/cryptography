"""
██╗░░░██╗██╗░██████╗░███████╗███╗░░██╗███████╗██████╗░███████╗
██║░░░██║██║██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔════╝
╚██╗░██╔╝██║██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝█████╗░░
░╚████╔╝░██║██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══╝░░
░░╚██╔╝░░██║╚██████╔╝███████╗██║░╚███║███████╗██║░░██║███████╗
░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚══════╝
"""

# repeat the key for the lenght of the text
def generate_key(text, keyword):
    return (keyword * (len(text)//len(keyword) + 1))[:len(text)]

# encrypt text with key
def encrypt_vigenere(text, key_word):
    key = generate_key(text, key_word)
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
def decrypt_vigenere(text, key_word):
    key = generate_key(text, key_word)
    plain = []
    for i in range(len(text)):
        if text[i].isalpha():
            c = (ord(text[i]) - ord(key[i]) + 26) % 26
            c += ord('A')
            plain.append(chr(c))
        else:
            plain.append(text[i])
    return "".join(plain)
