import pytest
from data_structures.doubly_linked_list import DoublyLinkedList, DoubleNode


def test_exists():
    assert DoublyLinkedList


def test_instantiate():
    assert DoublyLinkedList()


def test_empty_head():
    linked = DoublyLinkedList()
    assert linked.head is None


def test_populated_head():
    linked = DoublyLinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


def test_to_string_empty():
    linked_list = DoublyLinkedList()

    assert str(linked_list) == "NULL"


def test_to_string_single():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "NULL <-> { apple } <-> NULL"


def test_to_string_double():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "NULL <-> { apple } <-> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "NULL <-> { banana } <-> { apple } <-> NULL"


def test_includes_true():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


def test_includes_false():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def test_includes_empty_list():
    linked_list = DoublyLinkedList()

    assert not linked_list.includes(1)


def test_multiple_inserts():
    linked_list = DoublyLinkedList()

    linked_list.insert(7)
    linked_list.insert(linked_list.head.value)
    linked_list.insert(linked_list.head.value)

    assert str(linked_list) == "NULL <-> { 7 } <-> { 7 } <-> { 7 } <-> NULL"


def test_insert_none():
    linked_list = DoublyLinkedList()

    linked_list.insert(None)
    assert str(linked_list) == "NULL <-> { None } <-> NULL"


def test_head_has_no_prev():
    linked_list = DoublyLinkedList()

    linked_list.insert(1)

    assert not linked_list.head.prev_node
