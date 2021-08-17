from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree
from binary_search.binary_tree import breadth_first, BinaryTree, Node
import pytest


@pytest.fixture
def bt():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.left = Node(15)
    bt.root.right.left.right = Node(30)
    bt.root.right.left.left = Node(13)
    bt.root.right.right.left = Node(4)
    return bt


def test_fizz_buzz(bt):
    assert breadth_first(fizz_buzz_tree(bt)) == [
        '2', '7', 'Buzz', '2', 'Fizz', 'FizzBuzz', 'Fizz', 'Buzz', '11', '13', 'FizzBuzz', '4']


def test_fizz_buzz_empty_tree():
    bt = BinaryTree()
    assert breadth_first(fizz_buzz_tree(bt)) == breadth_first(bt)
