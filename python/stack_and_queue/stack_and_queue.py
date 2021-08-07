class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class StackEmptyException(Exception):
    pass


class Stack:

    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise Exception("Popping from empty stack")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if not self.top:
            raise Exception("Empty stack")
        return self.top.value

    def is_empty(self):
        return not self.top

    def __str__(self) -> str:
        string = ""
        current = self.top

        while current:
            string += f" {'{'}{str(current.value)}{'}'} -> "
            current = current.next
        string += "NULL"
        return string


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front and not self.rear:
            self.front = self.rear = node
        else:
            temp = self.rear
            self.rear = node
            temp.next = self.rear

    def dequeue(self):
        if not self.front and not self.rear:
            raise Exception("dequeuing from empty queue")
        temp = self.front
        self.front = self.front.next

        if(self.front == None):
            self.rear = None
        return temp.value

    def peek(self):
        if not self.front:
            raise Exception("Peeking To Empty Queue")
        return self.front.value

    def is_empty(self):
        return not self.rear

    def __str__(self) -> str:
        string = ""
        current = self.front
        while current:
            string += f" {'{'}{str(current.value)}{'}'} -> "
            current = current.next
        string += "NULL"
        return string


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    # print("Queue Front " + str(q.front.value))
    print("Queue Rear " + str(q))

    print(q.peek())
    print("Is Empty " + str(q.is_empty()))
