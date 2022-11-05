
from cesar import encrypt_cesar, decrypt_cesar

def process(data):
 # {"encrypt":true,"method":"Cesar","message":"Hello, world!","key":"3"}'
    if data['encrypt']:
        if data['method'] == "Cesar":
            result = encrypt_cesar(data['message'], int(data['key']))
            print(result)
            return result
        elif data['method'] == "Vigenere":
            print("oui")
    # decrypt mode
    else:
        if data['method'] == "Cesar":
            result = decrypt_cesar(data['message'], int(data['key']))
            print(result)
        else:
            print('we')