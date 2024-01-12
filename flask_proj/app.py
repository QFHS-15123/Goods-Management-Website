from datetime import datetime
import os

from flask import Flask, request, redirect, Response
from flask_cors import CORS

from database import db, Box, Goods
from flask_proj import box, goods
from flask_proj.tools import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gmw.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, supports_credentials=True)
db.init_app(app)


def create_table():
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        db.create_all()


app.register_blueprint(box.bp)
app.register_blueprint(goods.bp)


@app.route('/open_box', methods=['GET'])
def open_box():
    last_update_box = Box.query.order_by(Box.updated_time.desc()).first()
    box_name = last_update_box.name
    return box_name


if __name__ == '__main__':
    # create_table()
    app.run(debug=True)
