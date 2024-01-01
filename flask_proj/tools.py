import json
from static.static import *


def generate_response(data=None, message: str = SUCCESS_MESSAGE, status_code: int = SUCCESS_CODE) -> json:
    result = json.dumps({'message': message, 'status_code': status_code, 'data': data},
                        indent=2, ensure_ascii=False)  # ensure_ascii=False: Ensure the correct output of Chinese
    return result


def int2bool(data, col_name):
    for item in data:
        if item[col_name] == 1:
            item[col_name] = 'true'
        elif item[col_name] == 0:
            item[col_name] = 'false'
    return data


def bool2int(data, col_name):
    for item in data:
        if item[col_name] == 'true':
            item[col_name] = 1
        elif item[col_name] == 'false':
            item[col_name] = 0
    return data
