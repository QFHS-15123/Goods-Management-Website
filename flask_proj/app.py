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
    import goods
    app.register_blueprint(goods.bp)

    #     res = make_response(render_template('hello.html', error=error))
    #     res.status = '200'
    #     res.headers['Access-Control-Allow-Origin'] = "*"
    #     res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    #     return res

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.init_db_command()

