from binary_search.binary_tree import Node, BinaryTree


def tree_intersection(tree1, tree2):
    """
    This function take two tree as an input and return the common nodes between the two tree
    """
    # if one of the tree is empty return "No common elements"
    if not tree1.root:
        return "First tree empty"

    if not tree2.root:
        return "Second tree empty"

    # get trees elements using in_order return a list
    nodes_of_tree1 = tree1.in_order()
    nodes_of_tree2 = tree2.in_order()
    common_nodes = []
    # check the common nodes
    for item in nodes_of_tree1:
        if item in nodes_of_tree2:
            common_nodes.append(item)
    if len(common_nodes) > 0:
        return common_nodes
    else:
        return "No common elements"


if __name__ == "__main__":
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
    print(tree_intersection(bt, bt1))
