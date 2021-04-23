# Libraray Management System
import os
from search import search
from add_book import add_book
from check_user_info import user_info,book_id_info,check_due_date,check_borrow_list
from Edit_or_delete_file_line import remove_from_borrow_list
from add_detail import add_detail
from borrow import borrow
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
        id = input("\t\t\t\t\t\tEnter the Id: ")
        if user_info(id):
            while True:
                bookid = input("\t\t\t\t\t\tEnter the Book ID: ")
                if book_id_info(bookid):
                    borrow(id,bookid)
                    print("Thank you for visiting library. You Issued book for 7 days. if Not retured in time 10Rs/Day will be fined.\n")
                    break
                else:
                    print("\t\t\t\t\t\tSorry no book with this book id available!")
                    continue
        else:
            print("\t\t\t\t\t\tYour Entered ID is not in the list!")
            while True:
                yes_no=input("\t\t\t\t\t\tdo you want to add your details (y/n) : ")
                if yes_no == 'y':
                    id = int(input("\t\t\t\t\t\tEnter your University ID: "))
                    name = input("\t\t\t\t\t\tEnter your name: ")
                    phone = input("\t\t\t\t\t\tEnter your phone number: ")
                    location = input("\t\t\t\t\t\tEnter your location: ")
                    email = input("\t\t\t\t\t\tEnter your Email ID: ")
                    add_detail(id,name,phone,location,email)
                    break
                elif yes_no == 'n':
                    break
                else:
                    print("\t\t\t\t\t\tSorry wrong input!")
                    continue



    elif choice == 4:
        id = input('\t\t\t\t\t\tEnter University ID: ')
        if check_borrow_list(id):
            due_date = check_due_date(id)
            if due_date.days <=0:
                remove_from_borrow_list(id)
            else:
                fine = due_date.days * 10
                print("\n\t\t\t\t\t\tYou Have returned book late. So, you have to pay {}Rs fine.\n".format(fine))
                remove_from_borrow_list(id)

        else:
            print("\t\t\t\t\t\tName is not in the borrowed list!\n")


    elif choice == 5:


















    yes_no = input("\t\t\t\t\t\tDo you want to continue (y/n): ")
    if yes_no == 'y':
        continue
    else:
        quit()