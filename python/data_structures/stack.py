from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        temp = self.top
        self.top = Node(value, temp)

    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        popped = self.top
        self.top = popped.next
        return popped.value

    def is_empty(self):
        return not self.top

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

