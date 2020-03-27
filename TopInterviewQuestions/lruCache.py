class Node:
    def __init__(self, key, value):  # define a Linked list node that contains both key and value.
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.head = Node(-1, -1)  # Initial a Linked list with dummy head and dummy tail
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.store:
            return -1
        node = self.store[key]
        self._deleteNode(node)
        self._addNodeToFront(node)
        return node.val

    def put(self, key, value):
        node = self.store.get(key, None)  # if key is found, fetch this node, otherwise new a node by key and value
        if key in self.store:  # if key is found, delete it, and value need to be update in case it is changed
            self._deleteNode(node)
            node.val = value
            #node = Node(key, value)
        else:  # if the key is not found, put the new node to the storage dict
            node = Node(key, value)
            self.store[key] = node
        self._addNodeToFront(node)
        if len(
                self.store) > self.capacity:  # if total number exceeds capacity, delete the least used node next to the dummy tail
            last_node = self.tail.prev
            self._deleteNode(last_node)
            del self.store[last_node.key]

    def _addNodeToFront(self, node):
        old_first = self.head.next
        node.prev = self.head
        node.next = old_first
        self.head.next = node
        old_first.prev = node

    def _deleteNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

cache =LRUCache( 2 )

print(cache.put(2, 1))
print(cache.put(2, 2))
print(cache.get(2))
print(cache.put(1, 1))
print(cache.put(4, 1))
print(cache.get(2))
