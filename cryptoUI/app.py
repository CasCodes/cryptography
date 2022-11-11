from flask import Flask, render_template, request, jsonify
import flask
import json

# custom imports
from caesar import caesar
from vigenere import encrypt_vigenere, decrypt_vigenere

app = Flask(__name__)

# routes data to the correct mode and method
def pipeline(data) -> str:
 # {"encrypt":true,"method":"Cesar","message":"Hello, world!","key":"3"}'
    if data['method'] == 'RSA':
        return "RSA is not implemented yet!"
    if data['encrypt']:
        if data['method'] == "Caesar":
            result = caesar(data['message'], int(data['key']), 0)
            return result
        elif data['method'] == "Vigenere":
            result = encrypt_vigenere(data['message'].upper(), data['key'].upper())
            return result
    # decrypt mode
    else:
        if data['method'] == "Caesar":
            result = caesar(data['message'], int(data['key']), 1)
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