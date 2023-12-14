from flask import Blueprint, request

from db import get_db
from tools import *

bp = Blueprint('goods', __name__, url_prefix='/goods')


@bp.route('/', methods=['GET'])
def get_all_goods():
    box_name = request.args.get('box_name')
    box_name = '\'' + box_name + '\''
    db = get_db()
    res_data = []
    goods_list = (db.execute(f'SELECT * FROM {TABLE_NAME_GOODS} '
                             f'LEFT JOIN {TABLE_NAME_BOX} ON {TABLE_NAME_BOX}.{COL_NAME_ID_BOX} = {TABLE_NAME_GOODS}.{COL_NAME_BOX_ID_GOODS} '
                             f'WHERE {TABLE_NAME_BOX}.{COL_NAME_NAME_BOX} = {box_name};')
                  .fetchall())
    for goods in goods_list:
        goods.pop(COL_NAME_ID_GOODS)
        res_data.append(goods)
    return generate_response(data=res_data)
