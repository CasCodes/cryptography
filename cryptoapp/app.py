from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect/', methods = ['POST'])
def connect():
    if request.method == "POST":
        print("hi")
    return 

app.run(debug=True)