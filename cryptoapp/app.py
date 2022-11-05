from flask import Flask, render_template, request, jsonify
import flask
import json

# cutom imports
from crypto import process

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def revcieve_data():
    print("we")  # parse as JSON
    data = flask.request.get_data()
    print(data)

    # process the data
    process(json.loads(data))

    return jsonify({"status": 200})

if __name__ == "__main__":
    app.run(debug=True)