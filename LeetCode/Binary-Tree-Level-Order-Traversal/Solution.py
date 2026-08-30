1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def levelOrder(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: List[List[int]]
12        """
13        queue = deque([])
14        res = []
15
16        if root is None:
17            return res
18
19        queue.append(root)
20
21        while len(queue) != 0:
22            level = []
23
24            for i in range(len(queue)):
25                e = queue.popleft()
26
27                level.append(e.val)
28
29                if e.left is not None:
30                    queue.append(e.left)
31
32                if e.right is not None:
33                    queue.append(e.right)
34
35            res.append(level)
36
37        return res