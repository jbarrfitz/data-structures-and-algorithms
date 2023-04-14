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
        while curr_node:
            node_strings += f"{{ {curr_node.value} }} -> "
            curr_node = curr_node.next
        return f"{node_strings}NULL"

    def append(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head

    def includes(self, value):
        curr_node = self.head
        while curr_node:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        curr_node = self.head
        inserted = False
        if not curr_node:
            raise TargetError(f"No nodes in linked list to insert before")
        if curr_node.value == value:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
        else:
            while curr_node.next:
                if curr_node.next.value == value and not inserted:
                    old_next = curr_node.next
                    curr_node.next = new_node
                    new_node.next = old_next
                    inserted = True
                curr_node = curr_node.next
            if not inserted:
                raise TargetError(f"Value {value} not found in linked list")

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        curr_node = self.head
        inserted = False
        if not curr_node:
            raise TargetError(f"No nodes in linked list to insert after")
        while curr_node:
            if curr_node.value == value and not inserted:
                if curr_node.next:
                    old_next = curr_node.next
                    curr_node.next = new_node
                    new_node.next = old_next
                    inserted = True
                else:
                    curr_node.next = new_node
                    inserted = True
            curr_node = curr_node.next
        if not inserted:
            raise TargetError(f"Value {value} not found in linked list")

    def kth_from_end(self, k):
        if type(k) != int or k < 0:
            raise TargetError("Invalid input; k must be a non-negative integer")
        curr_node = self.head
        diff = 0
        while diff < k:
            curr_node = curr_node.next
            diff += 1
            if not curr_node:
                raise TargetError(
                    f"Linked list is not long enough to accommodate k of {k}")
        kth_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            kth_node = kth_node.next
        return kth_node.value

    def delete(self, value):
        # Handle empty linked list
        if self.head is None:
            raise TargetError(f"No nodes in linked list to delete")
        curr_node = self.head
        deleted = False
        # Handle deleting the head
        if curr_node.value == value:
            if curr_node.next:
                # if there are nodes after the head
                self.head == curr_node.next
                deleted = True
            else:
                # if the head is the only node
                self.head = None
                deleted = True
        while curr_node.next and not deleted:
            prev_node = curr_node
            curr_node = curr_node.next
            if curr_node.value == value:
                prev_node.next = curr_node.next
        if curr_node.value == value:
            prev_node.next = None


class Node:
    """
    Node belonging to a LinkedList. Contains its own value and a reference
    to the next node in the LinkedList.
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass


def zip_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    point1 = list1.head
    point2 = list2.head
    most_recent = None
    while point1 and point2:
        temp_next1 = point1.next
        temp_next2 = point2.next
        if not most_recent:
            most_recent = point1
            point1.next = point2
            most_recent = point2
        else:
            most_recent.next = point1.next
            point1.next = point2
            most_recent = point2
        point2.next = temp_next1
        point1 = temp_next1
        point2 = temp_next2
    if point1:
        most_recent.next = point1
    if point2:
        most_recent.next = point2
    return list1
