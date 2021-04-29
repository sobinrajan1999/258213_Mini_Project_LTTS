
# remove_from_borrow_list function to remove the info from the list
def remove_from_borrow_list(uid):
    borrow = open("borrow.csv", 'r', encoding='utf8')
    lines = borrow.readlines()
    borrow.close()

    borrow_new = open("borrow.csv", 'w', encoding='utf8')
    for line in lines:
        if line.split(',')[0] != uid:
            borrow_new.write(line)
    borrow_new.close()
