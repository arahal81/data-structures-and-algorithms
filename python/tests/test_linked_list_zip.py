from linked_list.linked_list import LinkedList, zipLists
import pytest


def test_link_list_zip_1(list_test_1, list_test_2):
    assert str(zipLists(list_test_1, list_test_2)
               ) == ' {2} ->  {7} ->  {9} ->  {4} -> NULL'


def test_link_list_zip_3(list_test_5, list_test_6):
    assert str(zipLists(list_test_5, list_test_6)
               ) == ' {2} ->  {5} ->  {3} ->  {6} ->  {4} ->  {1} ->  {9} -> NULL'


def test_link_list_zip_2(list_test_3, list_test_4):
    assert str(zipLists(list_test_3, list_test_4)
               ) == ' {2} ->  {5} ->  {3} ->  {6} ->  {4} -> NULL'


@pytest.fixture
def list_test_1():
    linked_list1 = LinkedList()
    linked_list1.append(2)
    linked_list1.append(9)
    return linked_list1


@pytest.fixture
def list_test_2():
    linked_list2 = LinkedList()
    linked_list2.append(7)
    linked_list2.append(4)
    return linked_list2


@pytest.fixture
def list_test_3():
    linked_list3 = LinkedList()
    linked_list3.append(2)
    linked_list3.append(3)
    linked_list3.append(4)
    return linked_list3


@pytest.fixture
def list_test_4():
    linked_list4 = LinkedList()
    linked_list4.append(5)
    linked_list4.append(6)
    return linked_list4


@pytest.fixture
def list_test_5():
    linked_list5 = LinkedList()
    linked_list5.append(2)
    linked_list5.append(3)
    linked_list5.append(4)
    return linked_list5


@pytest.fixture
def list_test_6():
    linked_list6 = LinkedList()
    linked_list6.append(5)
    linked_list6.append(6)
    linked_list6.append(1)
    linked_list6.append(9)
    return linked_list6
# import pytest
# from linked_list.linked_list import LinkedList
# from linked_list_zip.linked_list_zip import zipLists


# def test_ll_zip_1(list_test_1, list_test_2):
#     assert str(zipLists(list_test_1, list_test_2)
#                ) == ' {1} ->  {5} ->  {3} ->  {9} -> NULL'


# @pytest.fixture
# def list_test_1():
#     ll1 = LinkedList()
#     ll1.append(1)
#     ll1.append(3)

#     return ll1


# @pytest.fixture
# def list_test_2():
#     ll2 = LinkedList()
#     ll2.append(5)
#     ll2.append(9)

#     return ll2
