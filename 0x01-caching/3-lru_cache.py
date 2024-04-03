#!/usr/bin/env python3
""" This is a module that create a class LRUCache that inherits from
BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.lru_queue = []

    def print_cache(self):
        """Print the cache"""
        for key in self.lru_queue:
            print("{}: {}".format(key, self.cache_data[key]))

    def update_lru_queue(self, key):
        """Update LRU queue"""
        if key in self.lru_queue:
            self.lru_queue.remove(key)
        self.lru_queue.append(key)
        if len(self.lru_queue) > self.MAX_ITEMS:
            least_recently_used = self.lru_queue.pop(0)
            print("DISCARD:", least_recently_used)
            del self.cache_data[least_recently_used]

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.update_lru_queue(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.update_lru_queue(key)
        return self.cache_data[key]
