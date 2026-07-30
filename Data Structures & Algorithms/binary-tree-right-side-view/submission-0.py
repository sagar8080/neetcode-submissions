
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = deque([root])

        while queue:
            right = None
            qlen = len(queue)

            for i in range(qlen):
                node = queue.popleft()

                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if right:
                res.append(right.val)

        return res