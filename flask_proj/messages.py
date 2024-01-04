def SIMPLE_MSG(operation_code: int, signal: bool, name: str):
    operation = result = ''
    if operation_code == -1:
        operation = "delete"
    elif operation_code == 0:
        operation = "update"
    elif operation_code == 1:
        operation = "insert"
    if signal:
        result = 'Successfully'
    else:
        result = 'Fail to'
    return f'{result} {operation} {name}!'
