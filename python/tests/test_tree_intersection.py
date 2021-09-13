from binary_search.binary_tree import Node, BinaryTree
from tree_intersection.tree_intersection import tree_intersection


def test_common_nodes():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt.root = Node("100")
    bt.root.right = Node("200")
    bt.root.left = Node("250")
    bt.root.left.left = Node("300")
    bt.root.left.right = Node("10")
    bt1.root = Node("10")
    bt1.root.right = Node("175")
    bt1.root.left = Node("200")
    bt1.root.left.left = Node("205")
    bt1.root.left.right = Node("400")
    bt1.root.right.left = Node("250")


    assert ['10', '200', '250'] == tree_intersection(bt, bt1)



def test_first_tree_empty():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt1.root = Node("10")
    bt1.root.right = Node("175")
    bt1.root.left = Node("200")
    bt1.root.left.left = Node("205")
    bt1.root.left.right = Node("400")
    bt1.root.right.left = Node("250")

    assert "First tree empty" == tree_intersection(bt, bt1)


def test_second_tree_empty():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt.root = Node("100")
    bt.root.right = Node("200")
    bt.root.left = Node("250")
    bt.root.left.left = Node("300")
    bt.root.left.right = Node("10")

    assert "Second tree empty" == tree_intersection(bt, bt1)


def test_no_common_nodes():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt.root = Node("100")
    bt.root.right = Node("200")
    bt.root.left = Node("250")
    bt.root.left.left = Node("300")
    bt.root.left.right = Node("350")
    bt1.root = Node("10")
    bt1.root.right = Node("175")
    bt1.root.left = Node("210")
    bt1.root.left.left = Node("205")
    bt1.root.left.right = Node("400")
    bt1.root.right.left = Node("220")

    assert "No common elements" == tree_intersection(bt, bt1)
