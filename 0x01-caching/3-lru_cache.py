#!/usr/bin/env python3
""" This is a module that create a class LRUCache that inherits from
BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # If cache is full, discard the least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
