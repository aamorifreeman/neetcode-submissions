class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        
        self.head_dummy_lru = Node(None, None)
        self.tail_dummy_mru = Node(None, None)

        self.head_dummy_lru.next = self.tail_dummy_mru
        self.tail_dummy_mru.prev = self.head_dummy_lru

        self.key_to_node = {}
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        prev_node = self.tail_dummy_mru.prev

        node.prev = prev_node
        node.next = self.tail_dummy_mru

        prev_node.next = node
        self.tail_dummy_mru.prev = node


    def get(self, key: int) -> int:

        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.remove(node)
        self.insert(node)

        return node.value
        


    def put(self, key: int, value: int) -> None:

        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
        
        new_node = Node(key, value)
        self.insert(new_node)
        self.key_to_node[key] = new_node

        if len(self.key_to_node) > self.capacity:
            lru_node = self.head_dummy_lru.next
            
            self.remove(lru_node)
            del self.key_to_node[lru_node.key]

        
