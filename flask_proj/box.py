import datetime

from flask import Blueprint, request, jsonify

from database import db, Box
import static.mapping as mapping
from static.static import *
from tools import *

bp = Blueprint('box', __name__, url_prefix='/box')


@bp.route('/', methods=['GET'])
def get_all_boxes():
    boxes = Box.query.all()
    res_data = edit_query(db, boxes, drop_cols=['id'],datetime_cols=['updated_time', 'created_time'])
    return generate_response(data=res_data)


# @bp.route('/del', methods=['GET'])
# def delete():
#     box_name = request.args.get('box_name')
#     result = Box.query.filter(Box.name == box_name).update({'is_deleted': True})
#     # rows_changed = User.query.filter_by(role='admin').update(dict(permission='add_user'))
#     return insert_del_update_response(db, result, operation_code=0, name=box_name)
#
#
# @bp.route('/permanentlyDel', methods=['GET'])
# def permanently_delete():
#     box_name = request.args.get('box_name')
#     result = Box.query.filter(Box.name == box_name).delete()
#     return insert_del_update_response(db, result, operation_code=-1, name=box_name)
#
#
# @bp.route('/add', methods=['POST'])
# def add():
#     box = request.json['_value']
#     box['created_time'] = datetime.datetime.strptime(box['created_time'], '%Y-%m-%d %H:%M:%S')
#     box['updated_time'] = datetime.datetime.strptime(box['updated_time'], '%Y-%m-%d %H:%M:%S')
#     new_box = Box(name=box['name'], comment=box['comment'],
#                   created_time=box['created_time'], updated_time=box['updated_time'])
#     db.session.add(new_box)
#     db.session.commit()
#     return SIMPLE_MSG(1, True, new_box.name)
