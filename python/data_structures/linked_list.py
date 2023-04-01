class Node:
    """
    Node belonging to a LinkedList. Contains its own value and a reference
    to the next node in the LinkedList.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    """
    Structure containing nodes. This class contains only a reference to the
    head (first) node.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        curr_node = self.head
        node_strings = ""
        while curr_node is not None:
            if not node_strings:
                node_strings = f"{{ {curr_node.value} }}"
            else:
                node_strings = f"{node_strings} -> {{ {curr_node.value} }}"
            curr_node = curr_node.next_node
        if not node_strings:
            return "NULL"
        return f"{node_strings} -> NULL"

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next_node = old_head

    def includes(self, value):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False


class TargetError:
    pass
