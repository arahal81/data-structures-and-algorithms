from binary_search.binary_tree import Node, BinaryTree
from hash_map.hash_map import Hashmap
from stack_and_queue.stack_and_queue import Queue


def tree_intersection(tree1, tree2):
    """
    This function take two tree as an input and return the common nodes between the two tree
    """
    # if one of the tree is empty return "No common elements"
    if not tree1.root and not tree2.root:
        return "You passed two empty tree "

    if not tree1.root:
        return "First tree empty"

    if not tree2.root:
        return "Second tree empty"
    common_nodes = []
    ht = Hashmap()

    def breadth_first(tree, hash_table, first_tree=False):
        listcommon = []

        queque = Queue()
        queque.enqueue(tree.root)
        while not queque.is_empty():

            item = queque.dequeue()
            if first_tree:
                # add first tree to hash table
                hash_table.add(item.value, item.value)
            else:
                # check the common nodes
                if hash_table.contains(item.value):
                    listcommon += [item.value]
            if item.left if hasattr(item, 'left') else None:
                queque.enqueue(item.left)

            if item.right if hasattr(item, 'right') else None:
                queque.enqueue(item.right)
        return listcommon
    # get trees elements using in_order return a list
    _ = breadth_first(tree1, ht, True)
    common_nodes = breadth_first(tree2, ht)

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
    bt1.root = Node("12")
    bt1.root.right = Node("175")
    bt1.root.left = Node("200")
    bt1.root.left.left = Node("205")
    bt1.root.left.right = Node("400")
    bt1.root.right.left = Node("250")
    print(tree_intersection(bt, bt1))
