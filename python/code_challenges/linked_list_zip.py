def zip_lists(a, b):
    if not a.head:
        return b
    if not b.head:
        return a
    point1 = a.head
    point2 = b.head
    most_recent = None
    while point1 and point2:
        temp_next1 = point1.next
        temp_next2 = point2.next
        if not most_recent:
            point1.next = point2
            most_recent = point2
        else:
            most_recent.next = point1
            point1.next = point2
            most_recent = point2
        point2.next = temp_next1
        point1 = temp_next1
        point2 = temp_next2
    if point1:
        most_recent.next = point1
    if point2:
        most_recent.next = point2
    return a
