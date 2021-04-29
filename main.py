# Libraray Management System
# Some python files and libraries

#os library to clear screen
import os

# search file to search books in file through name
from search import search

#add book file to add book to the file
from add_book import add_book

# check_user_info file to check due dates,borrow list, book information, user information
from check_user_info import user_info,book_id_info,check_due_date,check_borrow_list

# edit_or_delete_file_line file to remove info from borrow file
from Edit_or_delete_file_line import remove_from_borrow_list

# add detail file to add details of a student
from add_detail import add_detail

# borrow file to add info of students who borrowed book
from borrow import borrow

#defaulter file to show info of those students who did not returned book in time
from defaulters import defaulters

# view_user_details file will show you user information
from view_user_details import view_user_detail

# sys file to add path to the file so to find the python files
from sys import path


# Infinite While loop to run the code until user wants to exit.
while True:

    #os.system to clear screen based on the operating system
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

    # choice 1 to search for the book.
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

        # here i have used yield to constanly retrieve book info from boooks.csv file
        for i in search(book_name):
            if i == 'not found':
                print("\n*                                                                                     Not found!                                                                       *\n")
            else:
                print(
                    "* {:<12}|  {:<40}|  {:<26}| {:<15} | {:<15} | {:<24} | {:<15} *".format(i[0], i[1][0:38],
                                                                                             i[2][0:24],
                                                                                             i[3],
                                                                                             i[4], i[5], i[6][0:13]))
        print(
            "************************************************************************************************************************************************************************")


    # choice 2 to add new book to the books.csv file
    elif choice == 2:
        book_Id = int(input("\t\t\t\t\t\tEnter the book ID: "))
        Name = input("\t\t\t\t\t\tEnter the name: ")
        Author = input("\t\t\t\t\t\tEnter Author name: ")
        lang_code = input("\t\t\t\t\t\tEnter language code: ")
        number_pages = int(input("\t\t\t\t\t\tEnter number of pages: "))
        publication_date = input("\t\t\t\t\t\tEnter Publication date: ")
        publisher_name = input("\t\t\t\t\t\tEnter Publisher's name: ")
        add_book(book_Id, Name, Author, lang_code, number_pages, publication_date, publisher_name)


    # choice 3 to borrow book from library
    elif choice == 3:
        id = input("\t\t\t\t\t\tEnter the Id: ")

        # checking for the university id in the list.
        # if user info is in the list then you can borrow book
        # else you have to add your details and then borrow book.
        if user_info(id):
            while True:
                bookid = input("\t\t\t\t\t\tEnter the Book ID: ")

                # checking for the book in book.csv file.
                # if book is in the list then you can borrow book
                # else book is not in the list and you can enter again.
                if book_id_info(bookid):
                    borrow(id,bookid)
                    print("\t\t\t\t\t\tThank you for visiting library. You Issued book for 7 days.\n\t\t\t\t\t\t if Not retured in time 10Rs/Day will be fined.\n")
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


    # choice 4 to return book
    elif choice == 4:
        id = input('\t\t\t\t\t\tEnter University ID: ')

        # checking for the university id in the list
        if check_borrow_list(id):
            due_date = check_due_date(id)

            # checking if the user returned book in time.
            if due_date.days <=0:
                remove_from_borrow_list(id)
                print("\t\t\t\t\t\tYou have returned the book. Knowledge is everything. Keep Learning!")
            else:
                fine = due_date.days * 10
                print("\n\t\t\t\t\t\tYou Have returned book late. So, you have to pay {}Rs fine.\n".format(fine))
                remove_from_borrow_list(id)

        else:
            print("\t\t\t\t\t\tName is not in the borrowed list!\n")

    # choice 5 to see those students who have not returned book in time.
    elif choice == 5:
        print(
            """
            *******************************************************************************************************************************
            *                                                                                                                             *
            *                                                          DEFAULTERS                                                         *
            *                                                                                                                             *
            *******************************************************************************************************************************
            *  University ID  |          Name          |      Phone Number      |     Book ID     |     Borrow Date    |    Return Date   *
            *******************************************************************************************************************************
            """
        )
        for line in defaulters():
            print("\t    *  {:<13}  |   {:<19}  |  {:<20}  |  {:<15}|  {:<18}|  {:<16}*".format(line[0],line[1],line[2],line[3],line[4],line[5]))
        print("""
            *******************************************************************************************************************************
        """
        )

    # choice 6 to see students information
    elif choice == 6:
        print("""
        **********************************************************************************************************************************************************
        *                                                                                                                                                        *
        *                                                              LIBRARY USER DETAILS                                                                      *
        *                                                                                                                                                        *
        **********************************************************************************************************************************************************
        *       University ID       |                    Name                  |         Phone Number        |      Location      |          Email ID            *  
        **********************************************************************************************************************************************************"""
        )
        for line in view_user_detail():
            print("        *  {:<23}  |   {:<37}  |  {:<25}  |  {:<16}  |  {:<26}  *".format(line[0],line[1],line[2],line[3],line[4]))
        print(
    """        **********************************************************************************************************************************************************
         """)

    # if you want to exit
    elif choice == 7:
        exit()

    # if you put a wrong input
    else:
        print("\t\t\t\t\t\tSorry Wrong input!")



    # yes_no to continue or exit
    yes_no = input("\n\t\t\t\t\t\tDo you want to continue (y/n): ")
    if yes_no == 'y':
        continue
    else:
        quit()