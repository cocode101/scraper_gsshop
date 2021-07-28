def insert_item():
    return "INSERT INTO item_list (collectdate, item_name, item_imageurl, item_price) " \
           "VALUES (%s,%s,%s,%s);"


def delete_all_item_data():
    return "DELETE FROM item_list WHERE 1 = 1;"


def delete_item_by_date(std_date):
    return "DELETE FROM item_list WHERE collectdate = {0}".format(std_date)


def select_all_items():
    return "SELECT * FROM item_list WHERE 1 = 1;"
