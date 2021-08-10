# from stack_and_queue.stack_and_queue import Stack
import re


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


def validate_brackets(string: str) -> bool:
    if not string:
        raise Exception("The input value is empty")
    usable_part = re.findall(r"\{|\}|\(|\)|\]|\[", string)
    if len(usable_part) % 2 != 0:
        return False
    else:
        stack = Stack()
        for char in usable_part:
            if char in ['[', '(', '{']:
                stack.push(char)
            else:
                if (char == '}' and stack.top.value == '{') or (char == ')' and stack.top.value == '(') or (char == ']' and stack.top.value == '['):
                    stack.pop()
                else:
                    return False
        if stack.top:
            return False
        else:
            return True


if __name__ == "__main__":
    print(validate_brackets("{}[{}]([)]"))
