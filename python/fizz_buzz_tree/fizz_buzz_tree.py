
from stack_and_queue.stack_and_queue import Queue
# from trees.trees import BinaryTree


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self, root=None):
        self.root = root


def fizz_buzz_tree(tree):
    if not tree.root:
        return tree
    queue = Queue()
    queue.enqueue(tree.root)
    new_tree = Tree()
    new_tree_node = Node(tree.root.value)
    new_tree.root = Tree(new_tree_node)
    new_tree = tree
    if new_tree.root.value % 5 == 0 and new_tree.root.value % 3 == 0:
        new_tree.root.value = 'FizzBuzz'
    elif new_tree.root.value % 3 == 0:
        new_tree.root.value = "Fizz"
    elif new_tree.root.value % 5 == 0:
        new_tree.root.value = "Buzz"
    else:
        new_tree.root.value = str(new_tree.root.value)

    def rec_func(node):
        if node.children:
            for i in range(len(node.children)):
                rec_func(node.children[i])
                if node.children[i].value % 3 == 0 and node.children[i].value % 5 == 0:
                    node.children[i].value = 'FizzBuzz'
                elif node.children[i].value % 3 == 0:
                    node.children[i].value = "Fizz"
                elif node.children[i].value % 5 == 0:
                    node.children[i].value = "Buzz"
                else:
                    node.children[i].value = str(node.children[i].value)
    rec_func(new_tree.root)

    return new_tree


def breadth_first(tree):
    if tree.root is None:
        return []
    queue = Queue()
    queue.enqueue(tree.root)
    output = []

    while not queue.is_empty():
        front = queue.dequeue()
        output.append(front.value)
        for i in range(len(front.children)):
            queue.enqueue(front.children[i])
    return output


if __name__ == "__main__":
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

    tree = Tree(node)
    print(breadth_first(tree))
    print(breadth_first(fizz_buzz_tree(tree)))
