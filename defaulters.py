from datetime import datetime
import re

def defaulters():
    borrow = open("borrow.csv", 'r', encoding='utf8')
    lines = borrow.readlines()
    lines.pop(0)
    for line in lines:
        list_1 = line.split(sep=',')
        pattern = r'\d{2}-\d{2}-\d{4}'
        today = datetime.today()
        today_date = today.strftime('%d-%m-%Y')
        match_borrow = re.search(pattern, today_date)
        borrow_date = datetime.strptime(match_borrow.group(), '%d-%m-%Y').date()
        match_return = re.search(pattern, list_1[-2])
        return_date = datetime.strptime(match_return.group(), '%d-%m-%Y').date()
        due_date = borrow_date - return_date
        if due_date.days > 0:
            yield list_1
    borrow.close()


