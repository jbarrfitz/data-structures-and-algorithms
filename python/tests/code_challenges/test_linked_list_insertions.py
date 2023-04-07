import pytest
from data_structures.linked_list import LinkedList, TargetError


# Rearranged these tests to group them in the order of the method being tested
def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"


def test_append_to_empty():
    # Jerry's Test
    linked_list = LinkedList()
    linked_list.append(7)
    assert str(linked_list) == "{ 7 } -> NULL"


def test_append_node_with_no_value():
    # Jerry's Test
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.append(None)
    assert str(linked_list) == "{ 3 } -> { 2 } -> { 1 } -> { None } -> NULL"


def test_append_affects_includes():
    # Jerry's Test
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.includes(1)


def test_append_multiple():
    # Jerry's Test
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    assert str(linked_list) == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"


def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"


def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_happens_only_once():
    # Jerry's Test
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.insert_before(2, 999)
    assert str(linked_list) == (
        "{ 1 } -> { 999 } -> { 2 } -> { 3 } -> { 2 } -> NULL")


@pytest.mark.skip("TODO")
def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


@pytest.mark.skip("TODO")
def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


# JERRY TESTS



