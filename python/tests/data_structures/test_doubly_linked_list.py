import pytest
from data_structures.doubly_linked_list import DoublyLinkedList


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


@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = DoublyLinkedList()

    assert str(linked_list) == "NULL"


@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


@pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


@pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = DoublyLinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")

@pytest.mark.skip("TODO")
def test_includes_empty_list():
    linked_list = DoublyLinkedList()

    assert not linked_list.includes(1)


@pytest.mark.skip("TODO")
def test_multiple_inserts():
    linked_list = DoublyLinkedList()

    linked_list.insert(7)
    linked_list.insert(linked_list.head.value)
    linked_list.insert(linked_list.head.value)

    assert str(linked_list) == "{ 7 } -> { 7 } -> { 7 } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_none():
    linked_list = DoublyLinkedList()

    linked_list.insert(None)
    assert str(linked_list) == "{ None } -> NULL"
