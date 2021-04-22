def add_book(bookid, name, author, lang, pages, date, publisher):
    book = open("books.csv", 'a')
    book.write(f"{bookid},{name},{author},{lang},{pages},{date},{publisher},")
    book.close()
