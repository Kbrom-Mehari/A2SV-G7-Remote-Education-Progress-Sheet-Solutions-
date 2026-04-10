class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        nxt = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = nxt
        nxt.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            existing = self.cache[key]
            self.remove(existing)
            del self.cache[key]

        node = Node(key, value)
        self.insert(node)

        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.right.prev
            del self.cache[lru.key]
            self.remove(lru)    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)