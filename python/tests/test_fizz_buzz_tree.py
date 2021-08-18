from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree, Node, Tree, breadth_first
import pytest


@pytest.fixture
def k_tree():
    node = Node(2)
    node.children += [Node(7)]
    node.children += [Node(5)]
    node.children[0].children += [Node(2)]
    node.children[0].children += [Node(4)]
    node.children[1].children += [Node(9)]
    node.children[1].children += [Node(8)]
    node.children[0].children[1].children += [Node(6)]
    node.children[0].children[1].children += [Node(10)]
    node.children[0].children[1].children += [Node(18)]
    node.children[0].children[1].children += [Node(15)]
    node.children[1].children[1].children += [Node(30)]

    k_tree = Tree(node)
    return k_tree


def test_fizz_buzz(k_tree):
    assert breadth_first(fizz_buzz_tree(k_tree)) == [
        '2', '7', 'Buzz', '2', '4', 'Fizz', '8', 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz', 'FizzBuzz']


def test_fizz_buzz_empty_tree():
    k_tree = Tree()
    assert breadth_first(fizz_buzz_tree(k_tree)) == breadth_first(k_tree)
