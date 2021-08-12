class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.list = None

    def pre_order(self):
        result = []

        def rec_fun(node):
            result.append(node.value)
            if node.left:
                rec_fun(node.left)
            if node.right:
                rec_fun(node.right)

        rec_fun(self.root)
        return result

    def in_order(self):
        result = []

        def rec_fun(node):
            if node.left:
                rec_fun(node.left)
            result.append(node.value)
            if node.right:
                rec_fun(node.right)

        rec_fun(self.root)
        return result

    def post_order(self):
        result = []

        def rec_fun(node):
            if node.left:
                rec_fun(node.left)
            if node.right:
                rec_fun(node.right)
            result.append(node.value)

        rec_fun(self.root)
        return result


class Binary_Search_Tree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = Node(value)

        else:
            def rec_func(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        rec_func(node.left)
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        rec_func(node.right)

            rec_func(self.root)

    def contains(self, value):

        if self.root:
            current = self.root

            def rec_func(current):
                if value == current.value:
                    return True
                elif value > current.value:
                    current = current.right
                    if current:
                        return rec_func(current)

                elif value < current.value:
                    current = current.left
                    if current:
                        return rec_func(current)

            if rec_func(current) == True:
                return True
            else:
                return False
        else:
            return False


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
    bt.root.right.right.left = Node(4)
    print(bt.pre_order())
    print(bt.in_order())
    print(bt.post_order())
    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(12)
    bst.add(9)
    bst.add(13)
    bst.add(8)
    bst.add(7)
    bst.add(6)
    print(bst.pre_order())
    print(bst.in_order())
    print(bst.post_order())
    print(bst.contains(13))
