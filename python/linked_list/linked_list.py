class Node:
    def __init__(self, value=""):
        self.value = value
        self.next = None

    def __add__(self, other):
        return Node(self.value + other.value)

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def includes(self, value):
        is_last = False
        current = self.head
        print(current)
        while not is_last:
            if str(current) == str(value):
                return True

            if current.next == None:
                is_last = True
            current = current.next
        return False

    def insert(self, value):
        node = Node(value)

        if self.head:
            node.next = self.head
        self.head = node

    def __str__(self) -> str:
        string = ""
        current = self.head

        while current:
            string += f" {'{'}{str(current.value)}{'}'} -> "
            current = current.next
        string += "NULL"
        return string


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    node1 = Node(1)
    node2 = Node(2)
    node3 = node1 + node2
    print(ll.includes(5))
