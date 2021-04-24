from datetime import datetime,timedelta
def borrow(id,bookid):
    name = ""
    phone = ""
    user_info = open("user_info.csv",'r',encoding='utf8')
    line = user_info.readlines()
    for i in line:
        line_sep = i.split(sep = ',')
        if line_sep[0] == id:
            name = line_sep[1]
            phone = line_sep[2]
            break
    file = open("borrow.csv",'a',encoding='utf8')
    today_date = datetime.today()
    due_date = timedelta(days= 7)
    due = today_date + due_date
    file.write("{},{},{},{},{},{},\n".format(id,name,phone,bookid,today_date.strftime("%d-%m-%Y"),due.strftime("%d-%m-%Y")))
