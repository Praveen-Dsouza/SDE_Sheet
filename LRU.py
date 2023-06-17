class Node: 
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to node
        
        #left = least recently used(LRU), right = most recently used 
        self.left, self.right = Node(0, 0), Node(0, 0)
        # we want the node to be connected
        self.left.next, self.right.prev = self.right, self.left
        
    # remove node from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    #insert node at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
        #we remove the value and then insert at the right of dll and return val else return -1
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #if we have key remove
        self.cache[key] = Node(key, value) #put a newNode in hashmap
        self.insert(self.cache[key]) 
        
        if len(self.cache) > self.cap:
            #remove from the list and delete the LRU from the hashmap
            lru = self.left.next #this will always have the lru
            self.remove(lru)
            del self.cache[lru.key]