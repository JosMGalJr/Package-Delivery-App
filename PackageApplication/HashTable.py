# Class for hash table, includes functions to add, update, lookup and remove items
class HashTable:
    def __init__(self, initial_capacity=20):
        self.list = [[] for _ in range(initial_capacity)]

    # Inserts new item into hash table, as well as updates key | O(n)
    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Looks up item in hash table | O(n)
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        return next((pair[1] for pair in bucket_list if key == pair[0]), None)

    # Removes item from hash table | O(n)
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        if key in destination:
            destination.remove(key)
