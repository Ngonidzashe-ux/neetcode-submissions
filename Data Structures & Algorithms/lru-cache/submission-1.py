
"""
Understand:
Match:
Plan:

Class Node:
    def __init__(self, key=0, value=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
Init:
self.cap = capacity
self.cache = {} #key to node
self.left = Node()
self.right = Node()
self.left.next = self.right
self.right.prev = self.left

Get:
Retrieve the value and update as MRU
if key in self.cache:
    self.remove(self.cache[key])
    self.insert(self.cache[key])
    return self.cache[key].val
return -1



Put:
if key in self.cache:
    self.cache[key].val = value
    self.remove(self.cache[key])
else:
    self.cache[key] = Node(key, value)
self.insert(self.cache[key])
if len(self.cache) > self.cap:
    self.remove(self.left.next)



If we have key already, update the value
else: create new key value pair
Then update this as MRU
If cache more than capacity, remove the LRU

Need to track MRU and LRU while preserving th order of everything


"""
class Node:
    def __init__(self, key=0, value=0, nxt=None, prev=None):
        self.key = key
        self.val = value
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #key to node
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
    def insert(self, node):
        prev = self.right.prev 
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node



        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value  # Update existing node's value
            self.remove(self.cache[key])  # Remove from current position
        else:
            self.cache[key] = Node(key, value)  # Create new node for new key
        self.insert(self.cache[key])  # Insert at front (most recently used)
        if len(self.cache) > self.cap:
            lru = self.left.next  # Least recently used node
            self.remove(lru)
            del self.cache[lru.key]  # Remove from hash map



