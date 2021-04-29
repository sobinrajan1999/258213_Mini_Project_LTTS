from datetime import datetime, timedelta


# borrow function to add borrowed books to borrow.csv file with the info of the user
def borrow(uid, book_id):
    name = ""
    phone = ""
    # taking information of student to add it to borrow.csv file
    user_info = open("user_info.csv", 'r', encoding='utf8')
    line = user_info.readlines()
    for i in line:
        line_sep = i.split(sep=',')
        if line_sep[0] == uid:
            name = line_sep[1]
            phone = line_sep[2]
            break
    file = open("borrow.csv", 'a', encoding='utf8')
    today_date = datetime.today()
    due_date = timedelta(days=7)
    due = today_date + due_date
    # appending the info to the file
    file.write("{},{},{},{},{},{},\n".format(uid, name, phone, book_id, today_date.strftime("%d-%m-%Y"),
                                             due.strftime("%d-%m-%Y")))
