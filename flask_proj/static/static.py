# Status code
SUCCESS_CODE = 200
ERROR_CODE = 400

# Request message
SUCCESS_MESSAGE = 'Success'
ERROR_MESSAGE = 'Fail'


def SUCCESS_ADD_BOX_MSG(box_name):
    return f'Successfully add box {box_name}!'


def FAIL_ADD_BOX_MSG(box_name):
    return f'Failed to add box {box_name}!'


def SUCCESS_ADD_GOODS_MSG(goods_name):
    return f'Successfully add goods {goods_name}!'


def UNKNOWN_ERROR_MSG():
    return 'Unknown error! Please contact the network administrator.'
