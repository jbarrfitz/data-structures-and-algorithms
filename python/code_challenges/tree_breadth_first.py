from collections import deque


def breadth_first(tree):
    if not tree.root:
        return []
    queue = deque()
    result = []
    queue.append(tree.root)
    while queue:
        curr_node = queue.popleft()
        result.append(curr_node.value)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
    return result
