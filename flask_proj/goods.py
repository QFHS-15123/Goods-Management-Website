from flask import Blueprint, request

from db import get_db
import static.mapping as mapping
from tools import *

bp = Blueprint('goods', __name__, url_prefix='/goods')


@bp.route('/', methods=['GET'])
def get_all_goods():
    box_name = request.args.get('box_name')
    db = get_db()
    res_data = []
    goods_list = (db.execute(mapping.query_all_goods(box_name)).fetchall())
    for goods in goods_list:
        goods.pop(mapping.GOODS_ID)
        res_data.append(goods)
    return generate_response(data=res_data)
