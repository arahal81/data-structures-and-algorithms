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

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        current_node = self.head
        if current_node.value == value:
            node.next = self.head
            self.head = node
        else:
            while current_node.next:
                if current_node.next.value == value:
                    node.next = current_node.next
                    current_node.next = node
                    break
                current_node = current_node.next

    def insert_after(self, value, new_value):
        node = Node(new_value)
        current_node = self.head
        while current_node:
            if current_node.value == value:
                temp = current_node.next
                current_node.next = node
                node.next = temp
                break
            current_node = current_node.next

    def kthFromEnd(self, k):
        current = self.head
        if current == None:
            return ("Empty List")

        if k <= -1:
            return("Negative number not acceptable")
        # values=[]
        # while current:
        #     values =values+ [current.value]
        #     current = current.next
        # print(values)
        # try:

        #     return values[::-1][k]
        idx = -1
        current = self.head
        while current:
            current = current.next
            idx = idx + 1
        if idx >= k:
            current = self.head
            for i in range(idx - k):
                current = current.next
            return current.value
        else:
            return ("Index not found")

    def __str__(self) -> str:
        string = ""
        current = self.head

        while current:
            string += f" {'{'}{str(current.value)}{'}'} -> "
            current = current.next
        string += "NULL"
        return string



def zipLists(list1, list2):
    if not list1.head:
        list1.head = list2.head
        list2.head = None

    current_item1 = list1.head
    current_item2 = list2.head
    flag = True
    while flag:
        if current_item1 and current_item2:
            pre_temp1 = current_item1
            temp1 = current_item1.next
            temp2 = current_item2.next
            if current_item1.next and current_item2.next:
                current_item1.next = current_item2
                current_item1 = temp1
                current_item2.next = current_item1
                current_item2 = temp2
            elif current_item1.next:
                current_item1.next = current_item2
                current_item1.next.next = temp1
                current_item2 = None

            elif current_item2.next:
                current_item1 = pre_temp1
                current_item1.next = current_item2
                current_item2 = None
            elif current_item2 and current_item1:
                current_item1.next = current_item2
                current_item2 = None
            elif current_item2:
                current_item1 = current_item2
                current_item2 = None
            else:
                flag = False
        elif current_item1:
            temp1 = current_item1.next
            if current_item1.next:
                current_item1 = current_item1.next
            elif current_item1:
                current_item1 = current_item2
                current_item2 = None
        elif current_item2:
            temp1 = current_item1.next
            if current_item2.next:
                current_item1 = pre_temp1
                current_item1 = current_item2.next
            elif current_item2:
                current_item1 = pre_temp1
                current_item1.next = current_item2
                current_item2 = None

        else:
            flag = False

    return list1


if __name__ == "__main__":

    linked_list1 = LinkedList()
    linked_list1.insert(2)
    linked_list1.insert(9)
    linked_list1.insert(3)
    linked_list1.insert(5)
    # linked_list1.insert(1)
    # linked_list1.insert(2)
    linked_list2 = LinkedList()
    linked_list2.insert(1)
    linked_list2.insert(7)
    linked_list2.insert(4)
    linked_list2.insert(0)
    # linked_list2.insert(1)
    # linked_list2.insert(2)
    print(zipLists(linked_list1, linked_list2))

