GET_ALL_BOXES = 'SELECT * FROM box;'

UPDATE_BOX = lambda box_cmt, box_name: "UPDATE box SET comment = '{}' WHERE name = '{}'".format(box_cmt, box_name)