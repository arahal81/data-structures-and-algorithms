from binary_search.binary_tree import Binary_Search_Tree, BinaryTree, Node
import pytest


@pytest.fixture
def binary_tree():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    return bt


@pytest.fixture
def binary_search_tree():
    bst = Binary_Search_Tree()
    return bst


# Can successfully instantiate an empty tree
def test_instantiate_an_empty_tree():
    bt = BinaryTree()
    assert bt.root == None


# Can successfully instantiate a tree with a single root node
def test_instantiate_a_tree_single_root_node():
    bt = BinaryTree()
    bt.root = Node(2)
    assert bt.root

# Can successfully add a left child and right child to a single root node


def test_instantiate_a_tree_single_root_node_right_left():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    assert bt.root and bt.root.left and bt.root.right


# Can successfully return a collection from a preorder traversal

def test_instantiate_a_tree_pre_order(binary_tree):

    assert binary_tree.pre_order() == [2, 7, 2, 6, 5, 11, 5, 9, 4]

# Can successfully return a collection from an inorder traversal


def test_instantiate_a_tree_in_order(binary_tree):

    assert binary_tree.in_order() == [2, 7, 5, 6, 11, 2, 5, 4, 9]
# Can successfully return a collection from a postorder traversal


def test_instantiate_a_tree_post_order(binary_tree):

    assert binary_tree.post_order() == [2, 5, 11, 6, 7, 4, 9, 5, 2]


# test add to binary search tree and contains
def test_add_contains_bst(binary_search_tree):
    binary_search_tree.add(5)
    output = binary_search_tree.contains(5)
    assert output == True


# test add to binary search tree and not contains
def test_add_not_contains_bst(binary_search_tree):
    binary_search_tree.add(7)
    output = binary_search_tree.contains(8)
    assert output == False


# test multi add to binary seaarch tree
def test_add_multi_node_bst(binary_search_tree):
    binary_search_tree.add(10)
    binary_search_tree.add(12)
    binary_search_tree.add(9)
    binary_search_tree.add(13)
    binary_search_tree.add(8)
    binary_search_tree.add(7)
    binary_search_tree.add(6)
    assert binary_search_tree.pre_order() == [10, 9, 8, 7, 6, 12, 13]


# “Happy Path” - Expected outcome
def test_maximum_happy_path(binary_tree):
    assert binary_tree.maximum_value() == 11


# Expected failure
def test_maximum_failure(binary_tree):
    assert binary_tree.maximum_value() != 9


# Edge Case (if applicable/obvious)
def test_maximum_failure():
    bt = BinaryTree()
    with pytest.raises(Exception, match="The tree is empty!"):
        bt.maximum_value()
