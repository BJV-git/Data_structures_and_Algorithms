# logic: have a dll, have teh pre-defined remove and add (at right).
# for get remove and add it
# for put, the dic will have the node info - if > cap remove the first node

class Node(object):
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev=None
        self.next = None

class LRUCache(object):
    def __init__(self,capacity):
        self.cap = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self,key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add_at_end(n)
            return n.val
        return -1

    def put(self,key,value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add_at_end(n)
        self.dic[key] = n
        if len(self.dic) > self.cap: # we will remove the first one
            n  = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self,node): # normal removing and adding the nodes
        p = node.prev # storing the both left and right and assigning to remove
        n = node.next
        p.next = n
        n.prev=p

    def _add_at_end(self,node):
        p = self.tail.prev # storing the tail prev and then all addings are new
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node





































#     def __init__(self, capacity):
#         self.size=0
#         self.inp =0
#         self.cap = capacity
#         self.position={}
#         self.lru={}
#
#     def get(self, key):
#         if key in self.lru:
#             return self.lru[key]
#         else:
#             return -1
#
#     def put(self, key, value):
#         if key in self.lru:
#             self.lru[key] = value
#             return
#         self.inp+=1
#         self.size+=1
#         self.position[self.inp] = key
#         if self.size > self.cap: # need to remove pos self.inp - self.cap
#             del self.lru[self.position[self.inp - self.cap]]
#
#             # del self.position[self.inp - self.cap]
#
#             self.size-=1
#         self.lru[key] = value
#         # print(self.lru, 'posuition',self.position)
#
#
# lru = LRUCache(2)
# lru.put(2,1)
# lru.put(2,2)
# print(lru.get(2))
# lru.put(1,1)
# lru.put(4,1)
# print(lru.get(2))



#
# lru = LRUCache(2)
# lru.put(1,1)
# lru.put(2,2)
# print(lru.get(1))
# lru.put(3,3)
# print(lru.get(2))
# lru.put(4,4)
# print(lru.get(1))
# print(lru.get(3))
# print(lru.get(4))