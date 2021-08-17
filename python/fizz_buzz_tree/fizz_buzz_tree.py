from binary_search.binary_tree import BinaryTree, Node, breadth_first


def fizz_buzz_tree(tree):

    temp_tree = tree
    if not temp_tree.root:
        temp_tree.root = Node(None)
        return temp_tree
    else:

        def rec_func(node):

            if node.value % 3 == 0 and node.value % 5 == 0:
                node.value = "FizzBuzz"
            elif node.value % 3 == 0:
                node.value = "Fizz"
            elif node.value % 5 == 0:
                node.value = "Buzz"
            else:
                node.value = str(node.value)
            if node.left:
                rec_func(node.left)
            if node.right:
                rec_func(node.right)

        rec_func(temp_tree.root)
        return temp_tree


if __name__ == "__main__":
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
    print(breadth_first(bt))
    print(breadth_first(fizz_buzz_tree(bt)))
