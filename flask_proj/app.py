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


# @app.route('/open_box', methods=['GET'])
# def home():
#     # box_name = request.args.get('box_name', default=None)
#     # if not box_name:
#     box_name = request.cookies.get('last_opened_box_name')
#     if not box_name:
#         last_update_box = Box.query.order_by(Box.updated_time.desc()).first()
#         box_name = last_update_box.name
#     return redirect(f'/goods/?box_name={box_name}', 302)
    # else:
    #     return None
# @app.route('/del', methods=['GET'])
# def delete_item():
#     return edit_is_deleted(request, True)
#
#
# @app.route('/permanentlyDel', methods=['GET'])
# def permanently_delete():
#     mode = request.args.get('mode')
#     name = request.args.get('name')
#     result = None
#     if mode == 'box':
#         result = Box.query.filter(Box.name == name).delete()
#     elif mode == 'goods':
#         result = Goods.query.filter(Goods.name == name).delete()
#     return insert_del_update_response(db, result, operation_code=-1, name=name)
#
#
# @app.route('/add', methods=['POST'])
# def add_item():
#     data = request.json['_value']
#     mode = data['mode']
#     data['created_time'] = datetime.strptime(data['created_time'], '%Y-%m-%d %H:%M:%S')
#     data['updated_time'] = datetime.strptime(data['updated_time'], '%Y-%m-%d %H:%M:%S')
#     new_item = None
#     if mode == 'box':
#         new_item = Box(name=data['name'], comment=data['comment'],
#                        created_time=data['created_time'], updated_time=data['updated_time'])
#     elif mode == 'goods':
#         new_item = Goods(name=data['name'], comment=data['comment'],
#                          created_time=data['created_time'], updated_time=data['updated_time'])
#     db.session.add(new_item)
#     db.session.commit()
#     return SIMPLE_MSG(1, True, new_item.name)
#
#
# @app.route('/restore', methods=['GET'])
# def restore_item():
#     return edit_is_deleted(request, False)
#
#
# def edit_is_deleted(request, is_deleted: bool):
#     mode = request.args.get('mode')
#     name_list = request.args.getlist('nameArray')
#     result = None
#     if mode == 'box':
#         result = Box.query.filter(Box.name == name_list[0]).update({'is_deleted': is_deleted})
#     elif mode == 'goods':
#         result = Goods.query.filter(Goods.name == name_list[0]).update({'is_deleted': is_deleted})
#     # rows_changed = User.query.filter_by(role='admin').update(dict(permission='add_user'))
#     return insert_del_update_response(db, result, operation_code=0, name=name)


if __name__ == '__main__':
    # create_table()
    app.run(debug=True)
