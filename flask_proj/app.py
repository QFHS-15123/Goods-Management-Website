from datetime import datetime
import os

from flask import Flask, request
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


@app.route('/del', methods=['GET'])
def delete_item():
    return edit_is_deleted(request, True)


@app.route('/permanentlyDel', methods=['GET'])
def permanently_delete():
    mode = request.args.get('mode')
    name = request.args.get('name')
    result = None
    if mode == 'box':
        result = Box.query.filter(Box.name == name).delete()
    elif mode == 'goods':
        result = Goods.query.filter(Goods.name == name).delete()
    return insert_del_update_response(db, result, operation_code=-1, name=name)


@app.route('/add', methods=['POST'])
def add_item():
    data = request.json['_value']
    mode = data['mode']
    data['created_time'] = datetime.strptime(data['created_time'], '%Y-%m-%d %H:%M:%S')
    data['updated_time'] = datetime.strptime(data['updated_time'], '%Y-%m-%d %H:%M:%S')
    new_item = None
    if mode == 'box':
        new_item = Box(name=data['name'], comment=data['comment'],
                       created_time=data['created_time'], updated_time=data['updated_time'])
    elif mode == 'goods':
        new_item = Goods(name=data['name'], comment=data['comment'],
                         created_time=data['created_time'], updated_time=data['updated_time'])
    db.session.add(new_item)
    db.session.commit()
    return SIMPLE_MSG(1, True, new_item.name)


@app.route('/restore', methods=['GET'])
def restore_item():
    return edit_is_deleted(request, False)


def edit_is_deleted(request, is_deleted: bool):
    mode = request.args.get('mode')
    name = request.args.get('name')
    result = None
    if mode == 'box':
        result = Box.query.filter(Box.name == name).update({'is_deleted': is_deleted})
    elif mode == 'goods':
        result = Goods.query.filter(Goods.name == name).update({'is_deleted': is_deleted})
    # rows_changed = User.query.filter_by(role='admin').update(dict(permission='add_user'))
    return insert_del_update_response(db, result, operation_code=0, name=name)


if __name__ == '__main__':
    # create_table()
    app.run(debug=True)

# def create_app(test_config=None):
#
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#
#
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'gmw.sqlite'),
#     )
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#

#
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.path.join(app.instance_path, 'gmw.sqlite')
#     database.init_app(app)
#
#     import box
#     app.register_blueprint(box.bp)
#     import goods
#
#
#     #     res = make_response(render_template('hello.html', error=error))
#     #     res.status = '200'
#     #     res.headers['Access-Control-Allow-Origin'] = "*"
#     #     res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
#     #     return res
#
#     return app
#
#
# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         db.create_all()
#     # with app.app_context():
#     #     db.init_db_command()
#
