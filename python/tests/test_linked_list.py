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
def test_linked_append(llt):
    llt.append(6)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{15}} ->  {{6}} -> NULL'

# Can successfully add multiple nodes to the end of a linked list

def test_linked_multiple_append(llt):
    llt.append(4)
    llt.append(7)
    llt.append(11)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{15}} ->  {{4}} ->  {{7}} ->  {{11}} -> NULL'

# Can successfully insert a node before a node located in the middle of a linked list

def test_linked_insert_before(llt):
    llt.insert_before(5,3)
    assert str(llt) == f' {{3}} ->  {{5}} ->  {{10}} ->  {{15}} -> NULL'

# Can successfully insert a node before the first node of a linked list

def test_linked_insert_before_first(llt):
    llt.insert_before(15,7)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{7}} ->  {{15}} -> NULL'

# Can successfully insert after a node in the middle of the linked list

def test_linked_insert_after(llt):
    llt.insert_after(10,8)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{8}} ->  {{15}} -> NULL'

# Can successfully insert a node after the last node of the linked list

def test_linked_insert_after_last(llt):
    llt.insert_after(15,20)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{15}} ->  {{20}} -> NULL'
def test_linked_values(llt):
    assert str(llt) == f" {{5}} ->  {{10}} ->  {{15}} -> NULL"

# this tests for negative input and indax not exist and happy path
@pytest.mark.parametrize(
    "input,expected_value",
    [
        (-5,"Negative number not acceptable"),
        (10,"Index not found"),
        (0,15),
        (1,10),
        (2,5),
    ],
)
def test_all_valid_dice_rolls(input, expected_value,llt):

    output = llt.kthFromEnd(input)
    print(output)
    assert output == expected_value

# this tests for empty linked list
def test_kthFromEnd_of_empty_linkedList():
    empty_ll=LinkedList()
    assert empty_ll.kthFromEnd(1) == "Empty List"
