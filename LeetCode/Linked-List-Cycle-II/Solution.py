1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        slow = head 
10        fast = head 
11        
12        while fast is not None and fast.next is not None:
13            slow = slow.next
14            fast = fast.next.next
15            
16            if(slow == fast):
17                slow = head
18                while(slow != fast):
19                    slow = slow.next
20                    fast = fast.next
21                return slow
22        
23        return None