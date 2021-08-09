from stack_and_queue.stack_and_queue import Stack


class PseudoQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):
        if self.temp_stack.top is None:
            if self.main_stack.top is None:
                raise Exception("dequeuing from empty queue")

            while self.main_stack.top:
                main_stack_top = self.main_stack.pop()
                self.temp_stack.push(main_stack_top)

            item_dequeued = self.temp_stack.pop()

            while self.temp_stack.top:
                temp_stack_top = self.temp_stack.pop()
                self.main_stack.push(temp_stack_top)

            return item_dequeued

    def __str__(self) -> str:
        string = ""
        current = self.main_stack.top

        while current:
            string += f" {'{'}{str(current.value)}{'}'} -> "
            current = current.next
        string += "NULL"
        return string
