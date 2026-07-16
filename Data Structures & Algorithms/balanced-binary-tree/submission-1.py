# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, node):
        if not node:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1
    
    def get_right_height(self, node):
        if not node:
            return 0
        return self.get_right_height(node.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        while queue:
            node = queue.popleft()
            lef_height = self.get_height(node.left)
            right_height = self.get_height(node.right)
            height_diff = abs(lef_height - right_height)
            if height_diff > 1:
                return False

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return True
        