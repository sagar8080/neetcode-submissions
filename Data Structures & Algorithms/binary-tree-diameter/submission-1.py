# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        if not root:
            return 0

        def get_height(node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        queue = deque([root])

        while queue:
            node = queue.popleft()

            left_height = get_height(node.left)
            right_height = get_height(node.right)
            diameter = left_height + right_height
            max_diameter = max(diameter, max_diameter)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return max_diameter