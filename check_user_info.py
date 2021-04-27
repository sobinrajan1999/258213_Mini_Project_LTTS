import re
from datetime import datetime


def user_info(uid):
    user = open("user_info.csv", 'r', encoding='utf8')
    user_list = user.readlines()
    for list_1 in user_list:
        line = list_1.split(sep=',')
        if uid == line[0]:
            user.close()
            return True
    user.close()
    return False


def book_id_info(book_id):
    user = open("books.csv", 'r', encoding='utf8')
    user_list = user.readlines()
    for list_1 in user_list:
        line = list_1.split(sep=',')
        if re.search(book_id, line[0]):
            user.close()
            return True
    user.close()
    return False


def check_borrow_list(uid):
    borrow = open("borrow.csv", 'r', encoding='utf8')
    lines = borrow.readlines()
    for line in lines:
        list_1 = line.split(sep=',')
        if list_1[0] == uid:
            borrow.close()
            return True
    borrow.close()
    return False


def check_due_date(uid):
    borrow = open("borrow.csv", 'r', encoding='utf8')
    lines = borrow.readlines()
    for line in lines:
        list_1 = line.split(sep=',')
        if list_1[0] == uid:
            pattern = r'\d{2}-\d{2}-\d{4}'
            today = datetime.today()
            today_date = today.strftime('%d-%m-%Y')
            match_borrow = re.search(pattern, today_date)
            borrow_date = datetime.strptime(match_borrow.group(), '%d-%m-%Y').date()
            match_return = re.search(pattern, list_1[-2])
            return_date = datetime.strptime(match_return.group(), '%d-%m-%Y').date()
            due_date = borrow_date - return_date
            return due_date
