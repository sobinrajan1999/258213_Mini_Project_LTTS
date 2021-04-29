# Library Management System
![library](https://www.stallionglobal.com/uploads/links/Title_68.jpg)

## Files and Descriptions
Sr no. | File                          | Description
-------|-------------------------------|------------------------------------------------------------------------
1      | `main.py`                     | Main part of this project. All py file work in this file
2      | `add_detail.py`               | to add student information of new student
3      | `borrow.py`                   | to add info of student who borrowed book from library
4      | `check_user_info.csv`         | Contain multiple functions to check for books, name, and id in the file
5      | `defaulter.py`                | to show students who have not submitted book in time
6      | `edit_or_delete_file_line.py` | to remove a name from the borrowed file who have returned book
7      | `add_book.py`                 | to add new book
8      | `search.py`                   | search book info from the books.csv file
9      | `view_user_info.py`           | to view students information


## CSV Files and Description
Sr no. | File                          | Columns
-------|-------------------------------|------------------------------------------------------------------------
1      | books.csv                     | `BookID` `title` `authors` `language_code`  `num_pages` `publication_date` `publisher`
2      | borrow.csv                    | `UniversityId` `Name` `Phone no.` `Book ID` `Borrow Date` `Return Date`
3      | user_info.csv                 | `UniversityID` `Name` `Phone` `Location` `Email ID`

## How to Run this Project
This folder contain a file named main.py that is calling the whole py files.
    
    python main.py

