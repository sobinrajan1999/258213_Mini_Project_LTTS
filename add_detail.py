def add_detail(id,name,phone,location,email):
    file = open("user_info.csv",'a',encoding='utf8')
    file.write("{},{},{},{},{},\n".format(id,name,phone,location,email))
    file.close()