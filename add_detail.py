def add_detail(uid, name, phone, location, email):
    file = open("user_info.csv", 'a', encoding='utf8')
    file.write("{},{},{},{},{},\n".format(uid, name, phone, location, email))
    file.close()
