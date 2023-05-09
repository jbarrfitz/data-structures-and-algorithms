import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree


def test_pre_order_empty():
    test_tree = BinaryTree()
    actual = test_tree.pre_order()
    expected = []
    assert actual == expected


def test_post_order_empty():
    test_tree = BinaryTree()
    actual = test_tree.post_order()
    expected = []
    assert actual == expected


def test_in_order_empty():
    test_tree = BinaryTree()
    actual = test_tree.in_order()
    expected = []
    assert actual == expected


def test_pre_order_with_null_values():
    test_tree = BinaryTree()
    test_tree.root = Node(None)
    test_tree.root.left = Node(1)
    test_tree.root.right = Node(2)
    actual = test_tree.pre_order()
    expected = [None, 1, 2]
    assert actual == expected


def test_post_order_with_null_values():
    test_tree = BinaryTree()
    test_tree.root = Node(None)
    test_tree.root.left = Node(1)
    test_tree.root.right = Node(2)
    actual = test_tree.post_order()
    expected = [1, 2, None]
    assert actual == expected


def test_in_order_with_null_values():
    test_tree = BinaryTree()
    test_tree.root = Node(None)
    test_tree.root.left = Node(1)
    test_tree.root.right = Node(2)
    actual = test_tree.in_order()
    expected = [1, None, 2]
    assert actual == expected

def test_pre_order_mixed_input_types():
    test_tree = BinaryTree()
    test_tree.root = Node("Hooray")
    test_tree.root.left = Node(9482)
    test_tree.root.right = Node([1, 2, 3])
    actual = test_tree.pre_order()
    expected = ["Hooray", 9482, [1, 2, 3]]


def test_post_order_mixed_input_types():
    test_tree = BinaryTree()
    test_tree.root = Node("Hooray")
    test_tree.root.left = Node(9482)
    test_tree.root.right = Node([1, 2, 3])
    actual = test_tree.post_order()
    expected = [9482, [1, 2, 3], "Hooray"]


def test_in_order_mixed_input_types():
    test_tree = BinaryTree()
    test_tree.root = Node("Hooray")
    test_tree.root.left = Node(9482)
    test_tree.root.right = Node([1, 2, 3])
    actual = test_tree.in_order()
    expected = [9482, "Hooray", [1, 2, 3]]
