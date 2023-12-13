import json
from flask import Blueprint

from db import get_db
from static.static import *

bp = Blueprint('box', __name__, url_prefix='/box')


@bp.route('/', methods=['GET'])
def get_all_boxes():
    db = get_db()
    response = dict()
    boxes = db.execute(f'SELECT * FROM {TABLE_NAME_BOX}').fetchall()
    for box in boxes:
        response[box[COL_BOX_ID]] = tuple(box[1:])
    return json.dumps(response, ensure_ascii=False)  # ensure_ascii=False: Ensure the correct output of Chinese
