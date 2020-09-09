class HashTableentries:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        self.entries = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return len(self.entries) / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
    # algorithm fnv-1 is
        # hash := FNV_offset_basis do
        # for each byte_of_data to be hashed
        #     hash := hash × FNV_prime
        #     hash := hash XOR byte_of_data
        # return hash
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed = FNV_offset_basis
        key_bytes = key.encode()
        for byte in key_bytes:
            hashed = hashed * FNV_prime
            hashed = hashed ^ byte
        return hashed

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for letter in key:
            hash = ((hash * 33) + hash + ord(letter))

        return (hash & 0xFFFFFFFF)
        # 0xFFFFFFFF means only return left 8 digits

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.entries[hash_index] != None:
            cur_node = self.entries[hash_index]
            if cur_node.key == key:
                self.entries[hash_index] = HashTableentries(key, value, cur_node.next)
            else:
                while cur_node.next is not None:
                    if cur_node.next.key == key:
                        cur_node.next = HashTableentries(key, value, cur_node.next)
                        return
                    else:
                        cur_node = cur_node.next
                cur_node.next = HashTableentries(key, value)
        else:
            self.entries[hash_index] = HashTableentries(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash = self.djb2(key)
        modded = hash % self.capacity
        if self.entries[modded] is None:
            print("Invalid key. Please input a valid entry.")
        else:
            cur_node = self.entries[modded]
            while cur_node is not None:
                if cur_node.key == key:
                    cur_node.value = None
                    return
                else:
                    cur_node = cur_node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash = self.djb2(key)
        modded = hash % self.capacity
        if self.entries[modded] is not None:
            if self.entries[modded].key == key:
                if self.entries[modded].value is not None:
                    return f"{self.entries[modded]}"
                else:
                    return None
            else:
                cur_node = self.entries[modded]
                while cur_node is not None:
                    if cur_node.key == key:
                        if cur_node.value is not None:
                            return f"{cur_node}"
                        else:
                            return None
                    else:
                        cur_node = cur_node.next
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        new_entries = self.entries
        self.entries = [None] * self.capacity
        for item in new_entries:
            if item.next is not None:
                cur_node = item.next
                while cur_node is not None:
                    self.put(cur_node.key, cur_node.value)
                    cur_node = cur_node.next
            self.put(item.key, item.value)
            


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
