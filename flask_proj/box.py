from flask import Blueprint

from db import get_db
from tools import *

bp = Blueprint('box', __name__, url_prefix='/box')


@bp.route('/', methods=['GET'])
def get_all_boxes():
    db = get_db()
    res_data = []
    boxes = db.execute(f'SELECT * FROM {TABLE_NAME_BOX}').fetchall()
    for box in boxes:
        box.pop(COL_NAME_ID_BOX)
        res_data.append(box)
    return generate_response(data=res_data)
