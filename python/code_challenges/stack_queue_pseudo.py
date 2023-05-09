from data_structures.stack import Stack


class EmptyQueue(Exception):
    pass

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None


class PseudoQueue:
    def __init__(self):
        self.primary_stack = Stack()
        self.secondary_stack = Stack()

    def enqueue(self, value):
        self.primary_stack.push(value)

    def dequeue(self):
        if not self.primary_stack:
            raise EmptyQueue("You cannot dequeue from an empty queue")
        while self.primary_stack:
            self.secondary_stack.push(self.primary_stack.pop())
        dequeued = self.secondary_stack.pop()
        while self.secondary_stack:
            self.primary_stack.push(self.secondary_stack.pop())
        return dequeued

