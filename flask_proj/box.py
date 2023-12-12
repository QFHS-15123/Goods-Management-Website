from flask import Blueprint
import xml.etree.ElementTree as ET

from db import get_db
from mapping.mapping import *

bp = Blueprint('box', __name__, url_prefix='/box')


@bp.before_app_request
def show_all_boxes():
    db = get_db()
    error = None

    print(UPDATE_BOX(1,2))
    # boxes = db.execute(GET_ALL_BOXES).fetchall()
    # print(boxes)
    # for i in boxes:
    #     print(i)
