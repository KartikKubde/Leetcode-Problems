1class Node:
2
3    def __init__(self, key, value):
4        self.key = key
5        self.value = value
6        self.prev = None
7        self.next = None
8
9class LRUCache(object):
10
11    def __init__(self, capacity):
12        """
13        :type capacity: int
14        """
15        self.capacity = capacity
16        self.cache = {}
17
18        self.head = Node(0,0)
19        self.tail = Node(0,0)
20        
21        self.head.next = self.tail
22        self.tail.prev = self.head
23
24    def remove(self,node):
25        node.prev.next = node.next
26        node.next.prev = node.prev
27        
28    def add_to_front(self,node):
29        node.next = self.head.next
30        node.prev = self.head
31        self.head.next.prev = node
32        self.head.next = node
33    
34    def get(self, key):
35        """
36        :type key: int
37        :rtype: int
38        """
39        if key not in self.cache:
40            return -1
41
42        target_node = self.cache[key]
43        self.remove(target_node)
44        self.add_to_front(target_node)
45        return target_node.value
46
47
48
49    def put(self, key, value):
50        """
51        :type key: int
52        :type value: int
53        :rtype: None
54        """
55        if key in self.cache:
56            target_node = self.cache[key]
57            target_node.value = value
58            self.remove(target_node)
59            self.add_to_front(target_node)
60
61        else:
62            new_node = Node(key,value)
63            self.cache[key] = new_node
64            self.add_to_front(new_node)
65
66            if len(self.cache) > self.capacity :
67                lru = self.tail.prev
68                self.remove(lru)
69                del self.cache[lru.key]
70    
71
72
73# Your LRUCache object will be instantiated and called as such:
74# obj = LRUCache(capacity)
75# param_1 = obj.get(key)
76# obj.put(key,value)
77
78