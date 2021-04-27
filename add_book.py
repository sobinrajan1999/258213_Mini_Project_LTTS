def add_book(book_id, name, author, lang, pages, date, publisher):
    book = open("books.csv", 'a')
    book.write(f"{book_id},{name},{author},{lang},{pages},{date},{publisher},\n")
    book.close()
