BOX_TABLE_NAME = 'box'
GOODS_TABLE_NAME = 'goods'

BOX_ID = GOODS_ID = 'id'
BOX_NAME = GOODS_NAME = 'name'
BOX_COMMENT = GOODS_COMMENT = 'comment'
BOX_CREATED_TIME = GOODS_CREATED_TIME = 'created_time'
BOX_UPDATED_TIME = GOODS_UPDATED_TIME = 'updated_time'
GOODS_STATUS = 'status'
GOODS_BOX_ID = 'box_id'
BOX_IS_DELETED = GOODS_IS_DELETED = 'is_deleted'


def query_all_boxes():
    return f'SELECT * FROM {BOX_TABLE_NAME};'


def query_all_goods(box_name):
    return f'SELECT * FROM {GOODS_TABLE_NAME} \
             LEFT JOIN {BOX_TABLE_NAME} ON {BOX_TABLE_NAME}.{BOX_ID} = {GOODS_BOX_ID} \
             WHERE {BOX_TABLE_NAME}.{BOX_NAME} = \'{box_name}\';'


def insert_box(box_name, box_comment, box_created_time, box_updated_time):
    return f'INSERT INTO {BOX_TABLE_NAME} \
             ({BOX_NAME}, {BOX_COMMENT}, {BOX_CREATED_TIME}, {BOX_UPDATED_TIME})\
              VALUES (\'{box_name}\', \'{box_comment}\', \'{box_created_time}\', \'{box_updated_time}\');'


def del_box(box_name):
    return f'UPDATE {BOX_TABLE_NAME} \
            SET {BOX_IS_DELETED} = 1 \
            WHERE {BOX_NAME} = \'{box_name}\';'
