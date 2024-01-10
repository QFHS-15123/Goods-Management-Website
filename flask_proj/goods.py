from datetime import datetime

from flask import Blueprint, request

from database import db, Goods, Box
import static.mapping as mapping
from tools import *

bp = Blueprint('goods', __name__, url_prefix='/goods')


@bp.route('/', methods=['GET'])
def get_all_goods():
    box_name = request.args.get('box_name')
    goods = (db.session.query(Goods).join(Box)
             .filter(Box.name == box_name, Goods.box_id == Box.id)
             .all())
    res_data = edit_query(db, goods, drop_cols=['id'], datetime_cols=['updated_time', 'created_time'])
    return generate_json(data=res_data)


# @bp.route('/edit', methods=['POST'])
# def edit():
#     box = request.json['_value']
#     box['created_time'] = datetime.datetime.strptime(box['created_time'], '%Y-%m-%d %H:%M:%S')
#     box['updated_time'] = datetime.datetime.strptime(box['updated_time'], '%Y-%m-%d %H:%M:%S')
#     result = Box.query.filter(Box.name == box['name']).update(box)
#     return insert_del_update_response(db, result, operation_code=1, name=box['name'])


@bp.route('/del', methods=['GET'])
def delete():
    box_name = request.args.get('box_name')
    goods_name = request.args.get('goods_name')
    result = (db.session.query(Goods).join(Box)
              .filter(Box.name == box_name, Goods.name == goods_name, Goods.box_id == Box.id)
              .update({'is_deleted': True}))
    # rows_changed = User.query.filter_by(role='admin').update(dict(permission='add_user'))
    return insert_del_update_response(db, result, operation_code=0, name=goods_name)


@bp.route('/permanentlyDel', methods=['GET'])
def permanently_delete():
    box_name = request.args.get('box_name')
    goods_name = request.args.get('goods_name')
    result = (db.session.query(Goods).join(Box)
              .filter(Box.name == box_name, Goods.name == goods_name, Goods.box_id == Box.id)
              .delete())
    return insert_del_update_response(db, result, operation_code=-1, name=goods_name)


@bp.route('/add', methods=['POST'])
def add():
    goods = request.json['_value']
    goods['created_time'] = datetime.strptime(goods['created_time'], '%Y-%m-%d %H:%M:%S')
    goods['updated_time'] = datetime.strptime(goods['updated_time'], '%Y-%m-%d %H:%M:%S')
    box_id = Box.query.filter(Box.name == goods['boxName']).first().id
    new_goods = Goods(name=goods['name'], comment=goods['comment'], status=goods['status'], box_id=box_id,
                      created_time=goods['created_time'], updated_time=goods['updated_time'])
    db.session.add(new_goods)
    db.session.commit()
    return SIMPLE_MSG(1, True, new_goods.name)


@bp.route('/update', methods=['GET'])
def update():
    box_name = request.args.get('box_name')
    goods_name = request.args.get('goods_name')
    col = request.args.get('col')
    value = request.args.get('value')
    result = (db.session.query(Goods).join(Box)
              .filter(Box.name == box_name, Goods.name == goods_name, Goods.box_id == Box.id)
              .update({col: value}))
    return insert_del_update_response(db, result, operation_code=0, name=goods_name)
