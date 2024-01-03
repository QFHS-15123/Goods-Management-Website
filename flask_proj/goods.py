from flask import Blueprint, request

from database import db, Goods, Box
import static.mapping as mapping
from tools import *

bp = Blueprint('goods', __name__, url_prefix='/goods')


@bp.route('/', methods=['GET'])
def get_all_goods():
    box_name = request.args.get('box_name')
    goods = (db.session.query(Goods).join(Box)
             .filter(Goods.box_id == Box.id)
             .filter(Box.name == box_name).all())
    res_data = edit_query(db, goods, drop_cols=['id'], datetime_cols=['updated_time', 'created_time'])
    return generate_response(data=res_data)
