import json
from static.static import *


def generate_response(data, message: str = SUCCESS_MESSAGE, status_code: int = SUCCESS_CODE) -> json:
    result = json.dumps({'message': message, 'status_code': status_code, 'data': data},
                        indent=2, ensure_ascii=False)  # ensure_ascii=False: Ensure the correct output of Chinese
    return result

