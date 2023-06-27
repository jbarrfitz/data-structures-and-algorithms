import pytest

from data_structures.hashtable import Hashtable


# Assuming the Hashtable class is defined and imported here

def test_set():
    table = Hashtable()
    table.set("name", "John")
    assert table.get("name") == "John"


def test_get_existing_key():
    table = Hashtable()
    table.set("name", "John")
    assert table.get("name") == "John"


def test_get_nonexistent_key():
    table = Hashtable()
    with pytest.raises(KeyError):
        table.get("age")


def test_keys():
    table = Hashtable()
    table.set("name", "John")
    table.set("age", 25)
    table.set("country", "USA")
    assert set(table.keys()) == {"name", "age", "country"}


def test_collision_handling():
    table = Hashtable()
    # Force a collision by setting two keys that have the same hash
    table.set("name", "John")
    table.set("mane", "Jane")
    assert table.get("name") == "John"
    assert table.get("mane") == "Jane"


def test_retrieve_value_from_bucket_with_collision():
    table = Hashtable()
    table.set("name", "John")
    table.set("mane", "Jane")
    assert table.get("name") == "John"
    assert table.get("mane") == "Jane"


def test_hash_in_range():
    table = Hashtable()
    key = "name"
    index = table.hash(key)
    assert 0 <= index < table.size
