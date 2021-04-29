import pytest

# check_user_info file to check due dates,borrow list, book information, user information
from check_user_info import user_info, book_id_info, check_due_date, check_borrow_list


def test_check_borrow_list():
    assert check_borrow_list("1710") == False
    assert check_borrow_list("1711") == True


def test_user_info():
    assert user_info("1710") == True
    assert user_info("1714") == False


def test_book_id_info():
    assert book_id_info("2") == True
    assert book_id_info("2020") == False
