from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, tail=None):
        self.front = front
        self.tail = tail

    def enqueue(self, value):
        if not self.tail:
            self.tail = self.front = Node(value)
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        dequeued = self.front.value
        self.front = self.front.next
        return dequeued

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        return not self.front

