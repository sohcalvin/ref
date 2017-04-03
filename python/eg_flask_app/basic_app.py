from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return "home success " ,200

if __name__ == '__main__':
    print("Running on localhost:5001")
    app.run(host='0.0.0.0', debug=True, port=5001, threaded=True)
    # app.run(host='0.0.0.0' port=8080, debug=True)
