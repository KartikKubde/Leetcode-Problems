# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head 
        my_set = set()  # sc O(n)

        while temp is not None:
            if temp in my_set:   # tc O(1)
                return True
            my_set.add(temp)   # tc O(1)
            temp = temp.next

        return False
