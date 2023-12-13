GET_ALL_BOXES = 'SELECT * FROM box;'

UPDATE_BOX = lambda box_name, box_cmt: "UPDATE box SET comment = '{}' WHERE name = '{}'".format(box_cmt, box_name)