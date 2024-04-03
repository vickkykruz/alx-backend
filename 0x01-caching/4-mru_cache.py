#!/usr/bin/env python3
""" This is a module that create a class MRUCache that inherits from
BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache """

    def __init__(self):
        """ Initialize MRU Cache """
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # If cache is full, discard the most recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.recently_used.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.recently_used.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        self.recently_used.remove(key)
        self.recently_used.append(key)
        return self.cache_data[key]
