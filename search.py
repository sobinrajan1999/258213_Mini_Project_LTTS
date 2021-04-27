import re


def search(search_name):
    book = open('books.csv', 'r', encoding='utf8')
    flag = False
    book_list = book.readlines()
    for list_1 in book_list:
        line = list_1.split(sep=',')
        line.pop()
        if re.search(search_name.upper(), line[1].upper()):  # search_name.upper() == line[1].upper()
            flag = True
            yield line
    if not flag:
        yield "not found"
    book.close()
