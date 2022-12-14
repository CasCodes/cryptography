from flask import Flask, render_template, request, jsonify
import flask
import json

# custom imports
from caesar import caesar
from vigenere import encrypt_vigenere, decrypt_vigenere
from rsa import generate_keys, rsa_decrypt, rsa_encrypt

app = Flask(__name__)

# routes data to the correct mode and method
def pipeline(data) -> str:
 # {"encrypt":true,"method":"Cesar","message":"Hello, world!","key":"3"}'
    if data['method'] == 'KEYS':
        return generate_keys()  
        
    # ENCRYPT
    if data['encrypt']:
        if data['method'] == "Caesar":
            result = caesar(data['message'], int(data['key']), 0)
            return result
        elif data['method'] == "Vigenere":
            result = encrypt_vigenere(data['message'].upper(), data['key'].upper())
            return result
        elif data['method'] == "RSA":
            pubk = tuple(data['key'][1])
            res = rsa_encrypt(pubk, data['message'])
            return res
    # DECRYPT
    else:
        if data['method'] == "Caesar":
            result = caesar(data['message'], int(data['key']), 1)
            return result
        elif data['method'] == "Vigenere":
            result = decrypt_vigenere(data['message'].upper(), data['key'].upper())
            return result
        elif data['method'] == "RSA":
             privk = tuple(data['key'][0])
             return rsa_decrypt(privk, data['message'])
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def revcieve_data():
    # parse as JSON
    data = flask.request.get_data()
    print(data)

    # process the data
    result = pipeline(json.loads(data))
    # return result to front end
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)