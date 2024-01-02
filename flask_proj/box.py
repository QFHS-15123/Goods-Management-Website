from flask import Blueprint, request, jsonify

from database import db
import static.mapping as mapping
from static.static import *
from tools import *
from database import Box

bp = Blueprint('box', __name__, url_prefix='/box')


@bp.route('/', methods=['GET'])
def get_all_boxes():
    boxes = query2dict(db, Box.query.all())
    res_data = []
    for box in boxes:
        box.pop("id")
        res_data.append(box)
    print(res_data)
    return generate_response(data=res_data)
    # db = get_db()
    # res_data = []
    # boxes = db.execute(mapping.query_all_boxes()).fetchall()
    # for box in boxes:
    #     box.pop(mapping.BOX_ID)
    #     res_data.append(box)
    # res_data = int2bool(res_data, mapping.BOX_IS_DELETED)
    # return generate_response(data=res_data)


@bp.route('/delBox', methods=['GET'])
def del_box():
    box_name = request.args.get('box_name')
    db = get_db()
    cursor = db.execute(mapping.del_box(box_name))
    if cursor.rowcount == 1:
        db.commit()
        return generate_response(message=SUCCESS_DEL_BOX_MSG(box_name))
    elif cursor.rowcount == 0:
        return generate_response(status_code=ERROR_CODE, message=FAIL_DEL_BOX_MSG(box_name))
    else:
        return generate_response(status_code=ERROR_CODE, message=UNKNOWN_ERROR_MSG())


@bp.route('/permanentlyDelBox', methods=['GET'])
def permanently_del_box():
    box_name = request.args.get('box_name')
    db = get_db()
    cursor = db.execute(mapping.permanently_del_box(box_name))
    if cursor.rowcount == 1:
        # db.commit()
        return generate_response(message=SUCCESS_PER_DEL_BOX_MSG(box_name))
    elif cursor.rowcount == 0:
        return generate_response(status_code=ERROR_CODE, message=FAIL_PER_DEL_BOX_MSG(box_name))
    else:
        return generate_response(status_code=ERROR_CODE, message=UNKNOWN_ERROR_MSG())


@bp.route('/addBox', methods=['POST'])
def add_box():
    db = get_db()
    box = request.json['_value']
    cursor = db.execute(mapping.insert_box(box_name=box['name'],
                                           box_comment=box['comment'],
                                           box_created_time=box['created_time'],
                                           box_updated_time=box['updated_time']))
    if cursor.rowcount == 1:
        return generate_response(message=SUCCESS_ADD_BOX_MSG(box['name']))
    elif cursor.rowcount == 0:
        return generate_response(status_code=ERROR_CODE, message=FAIL_ADD_BOX_MSG(box['name']))
    else:
        return generate_response(status_code=ERROR_CODE, message=UNKNOWN_ERROR_MSG())
