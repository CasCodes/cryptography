from flask import Flask, render_template, request, jsonify
import flask
import json

# cutom imports
from cesar import encrypt_cesar, decrypt_cesar
from vigenere import encrypt_vigenere, decrypt_vigenere

app = Flask(__name__)

# routes data to the correct mode and method
def pipeline(data) -> str:
 # {"encrypt":true,"method":"Cesar","message":"Hello, world!","key":"3"}'
    if data['encrypt']:
        if data['method'] == "Cesar":
            result = encrypt_cesar(data['message'], int(data['key']))
            print(result)
            return result
        elif data['method'] == "Vigenere":
            result = encrypt_vigenere(data['message'], data['key'])
            return result
    # decrypt mode
    else:
        if data['method'] == "Cesar":
            result = decrypt_cesar(data['message'], int(data['key']))
            return result
        elif data['method'] == "Vigenere":
            result = decrypt_vigenere(data['message'], data['key'])
            return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def revcieve_data():
    print("we")  # parse as JSON
    data = flask.request.get_data()
    print(data)

    # process the data
    result = pipeline(json.loads(data))

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)