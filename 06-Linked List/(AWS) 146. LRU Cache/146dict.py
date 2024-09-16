class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            lru = next(iter(self.dic))
            del self.dic[lru]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)