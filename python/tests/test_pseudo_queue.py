from pseudo_queue.pseudo_queue import PseudoQueue

import pytest


@pytest.fixture
def queue():
    queue = PseudoQueue()

    return queue

# Can successfully enqueue into a queue


def test_queue_enqueue_one_element(queue):
    queue.enqueue(1)
    assert str(queue) == f' {{1}} -> NULL'


# Can successfully enqueue multiple values into a queue
def test_queue_enqueue_multiple_element(queue):
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(9)
    assert str(queue) == f' {{9}} ->  {{4}} ->  {{1}} -> NULL'


# Can successfully dequeue out of a queue the expected value
def test_queue_pop_one_element(queue):
    queue.enqueue(4)
    queue.enqueue(5)
    assert 4 == queue.dequeue()


def test_dequeue_empty_queue_raises_exception(queue):
    with pytest.raises(Exception, match="dequeuing from empty queue"):
        queue.dequeue()
