from flask import Flask, render_template, request, jsonify
import flask
import json

# custom imports
from cesar import encrypt_cesar, decrypt_cesar
from vigenere import generate_key, encrypt_vigenere, decrypt_vigenere

app = Flask(__name__)

# routes data to the correct mode and method
def pipeline(data) -> str:
 # {"encrypt":true,"method":"Cesar","message":"Hello, world!","key":"3"}'
    if data['method'] == 'RSA':
        return "RSA is not implemented yet!"
    if data['encrypt']:
        if data['method'] == "Cesar":
            result = encrypt_cesar(data['message'], int(data['key']))
            return result
        elif data['method'] == "Vigenere":
            result = encrypt_vigenere(data['message'].upper(), data['key'].upper())
            return result
    # decrypt mode
    else:
        if data['method'] == "Cesar":
            result = decrypt_cesar(data['message'], int(data['key']))
            return result
        elif data['method'] == "Vigenere":
            result = decrypt_vigenere(data['message'].upper(), data['key'].upper())
            return result

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