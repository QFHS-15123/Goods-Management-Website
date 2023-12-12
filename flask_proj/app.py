import os
import sqlite3

from flask import Flask, request, render_template, make_response, g
from flask_cors import CORS
import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, supports_credentials=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'gmw.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    import box
    app.register_blueprint(box.bp)


    # a simple page that says hello
    # @app.route('/')
    # def hello_world():  # put application's code here
    #     return 'Hello World!'

    # @app.route('/login', methods=['POST', 'GET'])
    # def login():
    #     error = None
    #
    #     def valid_login(param, param1):
    #         print(1)
    #         return 1
    #
    #     def log_the_user_in(param):
    #         print('User login: ' + str(param))
    #
    #     if request.method == 'POST':
    #         if valid_login(request.form['username'],
    #                        request.form['password']):
    #             log_the_user_in(request.form['username'])
    #         else:
    #             error = 'Invalid username/password'
    #     # the code below is executed if the request method was GET or the credentials were invalid
    #     res = make_response(render_template('hello.html', error=error))
    #     res.status = '200'
    #     res.headers['Access-Control-Allow-Origin'] = "*"
    #     res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    #     return res

    return app


# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         db.init_db_command()

