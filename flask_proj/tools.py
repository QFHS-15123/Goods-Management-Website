import json
from static.static import *
from messages import *


def edit_query(db, query_data, drop_cols: list = None, datetime_cols: list = None):
    list_dict = query2dict(db, query_data)
    edited = []
    for data in list_dict:
        if drop_cols:
            for drop_col in drop_cols:
                data.pop(drop_col)
        if datetime_cols:
            for datetime_col in datetime_cols:
                data[datetime_col] = data[datetime_col].strftime('%Y-%m-%d %H:%M:%S')
        edited.append(data)
    return edited


def insert_del_update_response(db, update_result: int, operation_code: int, name: str) -> json:
    if update_result == 1:
        db.session.commit()
        return generate_json(message=SIMPLE_MSG(operation_code, True, name))
    elif update_result == 0:
        return generate_json(status_code=ERROR_CODE, message=SIMPLE_MSG(operation_code, False, name))
    else:
        return generate_json(status_code=ERROR_CODE, message=UNKNOWN_ERROR_MSG())


def generate_json(data=None, message: str = SUCCESS_MESSAGE, status_code: int = SUCCESS_CODE) -> json:
    return json.dumps({'message': message, 'status_code': status_code, 'data': data},
                      indent=2, ensure_ascii=False)  # ensure_ascii=False: Ensure the correct output of Chinese


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


def query2dict(db, model_list):
    if isinstance(model_list, list):  # 如果传入的参数是一个list类型的，说明是使用的all()的方式查询的
        if isinstance(model_list[0], db.Model):  # 这种方式是获得的整个对象  相当于 select * from table
            lst = []
            for model in model_list:
                dic = {}
                for col in model.__table__.columns:
                    dic[col.name] = getattr(model, col.name)
                lst.append(dic)
            return lst
        else:  # 这种方式获得了数据库中的个别字段  相当于select id,name from table
            lst = []
            for result in model_list:  # 当以这种方式返回的时候，result中会有一个keys()的属性
                lst.append([dict(zip(result.keys, r)) for r in result])
            return lst
    else:  # 不是list,说明是用的get() 或者 first()查询的，得到的结果是一个对象
        if isinstance(model_list, db.Model):  # 这种方式是获得的整个对象  相当于 select * from table limit=1
            dic = {}
            for col in model_list.__table__.columns:
                dic[col.name] = getattr(model_list, col.name)
            return dic
        else:  # 这种方式获得了数据库中的个别字段  相当于select id,name from table limit = 1
            return dict(zip(model_list.keys(), model_list))
