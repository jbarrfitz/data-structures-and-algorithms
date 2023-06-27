class Hashtable:
    """Hashtable class that implements a hash table data structure."""

    def __init__(self):
        """
        Initialize the Hashtable.

        The size of the hashtable is set to 1000, and the hashtable is initialized as a list of empty lists.
        """
        self.size = 1000  # Size of the hashtable
        self.table = [[] for _ in range(self.size)]  # Initialize the hashtable as a list of empty lists

    def _hash(self, key):
        """
        Compute the hash value for the given key.

        Args:
            key: The key to be hashed.

        Returns:
            The index in the hashtable where the key should be stored.
        """
        return hash(key) % self.size  # Compute the hash value of the key

    def set(self, key, value):
        """
        Set a key-value pair in the hashtable.

        If the key already exists, its value is replaced with the given value.

        Args:
            key: The key to be stored.
            value: The value associated with the key.

        Returns:
            None
        """
        index = self._hash(key)  # Get the index for the key
        for entry in self.table[index]:
            if entry[0] == key:  # If the key already exists, replace its value
                entry[1] = value
                return
        self.table[index].append([key, value])  # Add a new key-value pair to the table

    def get(self, key):
        """
        Get the value associated with the given key in the hashtable.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key does not exist in the hashtable.
        """
        index = self._hash(key)  # Get the index for the key
        for entry in self.table[index]:
            if entry[0] == key:  # If the key exists, return its value
                return entry[1]
        raise KeyError(f"Key '{key}' does not exist in the hashtable")  # Key does not exist

    def has(self, key):
        """
        Check if the given key exists in the hashtable.

        Args:
            key: The key to check for existence.

        Returns:
            True if the key exists in the hashtable, False otherwise.
        """
        index = self._hash(key)  # Get the index for the key
        for entry in self.table[index]:
            if entry[0] == key:  # If the key exists, return True
                return True
        return False  # Key does not exist

    def keys(self):
        """
        Get all the keys stored in the hashtable.

        Returns:
            A collection of keys.
        """
        keys = []
        for bucket in self.table:
            for entry in bucket:
                keys.append(entry[0])  # Append the key to the list of keys
        return keys

    def hash(self, key):
        """
        Get the index in the hashtable for the given key.

        Args:
            key: The key to get the index for.

        Returns:
            The index in the hashtable where the key is stored.
        """
        return self._hash(key)  # Return the index in the collection for the key
