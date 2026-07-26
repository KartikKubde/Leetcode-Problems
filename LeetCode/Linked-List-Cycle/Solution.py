1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        temp = head 
10        my_set = set()  # sc O(n)
11
12        while temp is not None:
13            if temp in my_set:   # tc O(1)
14                return True
15            my_set.add(temp)   # tc O(1)
16            temp = temp.next
17
18        return False
19