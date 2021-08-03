from linked_list_zip.linked_list_zip import zipLists
from linked_list.linked_list import LinkedList
import pytest


def test_ll_zip_1(list_test_1, list_test_2, list_test_3, list_test_4):
    assert str(zipLists(list_test_1, list_test_2)
               ) == ' {2} ->  {7} ->  {9} ->  {4} -> Null'
    assert str(zipLists(list_test_3, list_test_4)
               ) == ' {2} ->  {5} ->  {3} ->  {6} ->  {4} -> Null'


@pytest.fixture
def list_test_1():
    linked_list1 = LinkedList()
    linked_list1.append(2)
    linked_list1.append(9)
    return list_test_1


@pytest.fixture
def list_test_2():
    linked_list2 = LinkedList()
    linked_list2.append(7)
    linked_list2.append(4)
    return list_test_2


@pytest.fixture
def list_test_3():
    linked_list3 = LinkedList()
    linked_list3.append(2)
    linked_list3.append(3)
    linked_list3.append(4)
    return list_test_3


@pytest.fixture
def list_test_4():
    linked_list4 = LinkedList()
    linked_list4.append(5)
    linked_list4.append(6)
    return list_test_4
