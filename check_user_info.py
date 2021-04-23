import re


def user_info(id):
    user = open("user_info.csv", 'r', encoding='utf8')
    user_list = user.readlines()
    for list_1 in user_list:
        line = list_1.split(sep=',')
        if id == line[0]:
            user.close()
            return True
    user.close()
    return False


def book_id_info(bookid):
    user = open("books.csv", 'r', encoding='utf8')
    user_list = user.readlines()
    for list_1 in user_list:
        line = list_1.split(sep=',')
        if re.search(bookid, line[0]):
            return True
    user.close()
    return False
