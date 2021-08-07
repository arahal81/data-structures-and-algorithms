from stack_and_queue.stack_and_queue import Queue, Stack
import pytest

# Stack Object


@pytest.fixture
def stack():
    stack = Stack()

    return stack

# Queue Object


@pytest.fixture
def queue():
    queue = Queue()

    return queue


# Can successfully push onto a stack
def test_stack_pushing_one_element(stack):
    stack.push(1)
    assert stack.top.value == 1


# Can successfully push multiple values onto a stack
def test_stack_pushing_multiple_element(stack):
    stack.push(1)
    stack.push(4)
    stack.push(9)
    assert stack.top.value == 9


# Can successfully pop off the stack
def test_stack_pop_one_element(stack):
    stack.push(4)
    stack.push(5)
    assert 5 == stack.pop()


# Can successfully empty a stack after multiple pops

def test_stack_is_empty(stack):
    stack.push(1)
    stack.push(1)
    assert stack.is_empty() == False
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True


# Can successfully peek the next item on the stack
def test_stack_peek(stack):
    stack.push(1)
    stack.push(4)
    stack.push(9)
    assert stack.peek() == 9

# Can successfully instantiate an empty stack


def test_instantiate_empty_stack(stack):
    assert stack.is_empty()

# Calling pop or peek on empty stack raises exception


def test_peek_empty_stack_raises_exception(stack):
    with pytest.raises(Exception, match="Empty stack"):
        stack.peek()


# Can successfully enqueue into a queue
def test_queue_enqueue_one_element(queue):
    queue.enqueue(1)
    assert queue.rear.value == 1


# Can successfully enqueue multiple values into a queue
def test_queue_enqueue_multiple_element(queue):
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(9)
    assert queue.front.value == 1 and queue.rear.value == 9


# Can successfully dequeue out of a queue the expected value
def test_queue_pop_one_element(queue):
    queue.enqueue(4)
    queue.enqueue(5)
    assert 4 == queue.dequeue()


# Can successfully peek into a queue, seeing the expected value
def test_peek_queue(queue):
    queue.enqueue(4)
    queue.enqueue(5)
    assert 4 == queue.peek()


# Can successfully empty a queue after multiple dequeues
def test_queue_is_empty(queue):
    queue.enqueue(1)
    queue.enqueue(5)
    assert queue.is_empty() == False
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True


# Can successfully instantiate an empty queue
def test_instantiate_empty_queue(queue):
    assert queue.is_empty()


# Calling dequeue or peek on empty queue raises exception
def test_peek_empty_queue_raises_exception(queue):
    with pytest.raises(Exception, match="Peeking To Empty Queue"):
        queue.peek()


def test_dequeue_empty_queue_raises_exception(queue):
    with pytest.raises(Exception, match="dequeuing from empty queue"):
        queue.dequeue()
