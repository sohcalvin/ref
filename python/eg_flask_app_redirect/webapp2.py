from flask import Flask, redirect
app1 = Flask(__name__)

@app1.route('/redirect', methods = ['POST', 'GET'])
def home():
    return redirect('http://localhost:5001', code=307)

@app1.route('/', methods = ['POST', 'GET'])
def post_page() :
    return  '''
     <html>
     <form method="POST" action="/redirect">
        <input type="submit" value="Submit">
    </form>
     ''',200

if __name__ == '__main__':
    print("Running on localhost:5002")
    app1.run(host='0.0.0.0', debug=True, port=5002, threaded=True)
