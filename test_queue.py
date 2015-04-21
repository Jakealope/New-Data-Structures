from queue import Queue


def test_enqueue_first_item():
    queue = Queue()
    queue.enqueue("Bacon")
    assert queue.last.val == "Bacon"


def test_enqueue_multi_last_item():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Steak")
    queue.enqueue("Beer")
    assert queue.last.val == "Beer"
