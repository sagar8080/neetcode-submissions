# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)

        if min_val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif max_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return root