from flask import Flask, request, render_template, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def valid_login(param, param1):
    print(1)
    return 1


def log_the_user_in(param):
    print('User login: ' + str(param))


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method was GET or the credentials were invalid
    res = make_response(render_template('hello.html', error=error))
    res.status = '200'
    res.headers['Access-Control-Allow-Origin'] = "*"
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    return res


if __name__ == '__main__':
    app.run()
