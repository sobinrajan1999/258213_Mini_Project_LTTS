# view_user_detail function to show students information
def view_user_detail():
    user_info = open('user_info.csv', 'r', encoding='utf8')
    lines = user_info.readlines()
    for line in lines:
        list_1 = line.split(',')
        list_1.pop()
        yield list_1
