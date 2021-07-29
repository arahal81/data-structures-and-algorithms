from linked_list.linked_list import LinkedList, Node

import pytest


def test_instantiate():
    linked_list = LinkedList()
    assert isinstance(linked_list, LinkedList)


def test_insert():
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(12)
    print(ll.head.value)
    assert ll.head.value == 12


def test_head(llt):
    assert llt.head.value == 5
    assert llt.head.next.value == 10


def test_include(llt):
    assert llt.includes(9) == False
    assert llt.includes(10) == True


def test_linked_values(llt):
    assert str(llt) == f" {{5}} ->  {{10}} ->  {{15}} -> NULL"


@pytest.fixture
def llt():
    linked_list = LinkedList()
    linked_list.insert(15)
    linked_list.insert(10)
    linked_list.insert(5)
    return linked_list
