from flask import Flask, redirect
app1 = Flask(__name__)

@app1.route('/', methods = ['POST', 'GET'])
def home():
    return 'home success', 200

if __name__ == '__main__':
    print("Running on localhost:5001")
    app1.run(host='0.0.0.0', debug=True, port=5001, threaded=True)
