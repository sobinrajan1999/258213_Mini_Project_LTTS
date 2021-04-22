# Libraray Management System
import os
from search import search
from add_book import add_book
from check_user_info import user_info,book_id_info
from sys import path

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        """
                             ***************************************************************************
                             *                                                                         *
                             *                        WELCOME TO LIBRARY MANAGER                       *
                             *                                                                         *
                             ***************************************************************************
                             *                                                                         *
                             *                           1. Book Availability                          *
                             *                           2. Add new book                               *
                             *                           3. Borrow Books                               *
                             *                           4. Return Books                               *
                             *                           5. Defaulters                                 *
                             *                           6. View User Details                          *
                             *                           7. Exit                                       *
                             ***************************************************************************  
        """
    )
    choice = int(input("\t\t\t\t\t\tEnter your choice(1-6) : "))
    if choice == 1:
        book_name = input("\t\t\t\t\t\tEnter the name of the book: ")
        print(
            """
************************************************************************************************************************************************************************
*                                                                                                                                                                      *
*                                                                             SEARCH RESULT                                                                            *
*                                                                                                                                                                      *
************************************************************************************************************************************************************************
*   Book ID   |                    Name                  |           Authors          |  Language_code  |  No. of pages   |     Publication date     |    Publisher    *  
************************************************************************************************************************************************************************"""
        )
        for i in search(book_name):
            print(
                "* {:<12}|  {:<40}|  {:<26}| {:<15} | {:<15} | {:<24} | {:<15} *".format(i[0], i[1][0:38], i[2][0:24],
                                                                                         i[3],
                                                                                         i[4], i[5], i[6][0:13]))
        print(
            "************************************************************************************************************************************************************************")



    elif choice == 2:
        book_Id = int(input("\t\t\t\t\t\tEnter the book ID: "))
        Name = input("\t\t\t\t\t\tEnter the name: ")
        Author = input("\t\t\t\t\t\tEnter Author name: ")
        lang_code = input("\t\t\t\t\t\tEnter language code: ")
        number_pages = int(input("\t\t\t\t\t\tEnter number of pages: "))
        publication_date = input("\t\t\t\t\t\tEnter Publication date: ")
        publisher_name = input("\t\t\t\t\t\tEnter Publisher's name: ")
        add_book(book_Id, Name, Author, lang_code, number_pages, publication_date, publisher_name)



    elif choice == 3:
        while True:
            name = input("\t\t\t\t\t\tEnter the name: ")
            if user_info(name):
                phone = input("\t\t\t\t\t\tEnter Phone number: ")
                while True:
                    book_Id = input("\t\t\t\t\t\tEnter the Book ID: ")
                    if book_id_info(book_Id):
                        pass
                    else:
                        break
            else:
                print("\t\t\t\t\t\tYour Entered name is not in the list!")
                yes_no=input("\t\t\t\t\t\tdo you want to add your details (y/n) : ")
                if yes_no == 'y':
                    #to be continued














    yes_no = input("\t\t\t\t\t\tDo you want to continue (y/n): ")
    if yes_no == 'y':
        continue
    else:
        quit()