# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        # Add the root to the queue
        queue = deque([root])

        # Process the queue while the queue is full
        while queue:
            # get the node
            node = queue.popleft()
            # swap the node elements left, right = right, left
            node.left, node.right = node.right, node.left

            # if node has left append it to the queue   
            if node.left:
                queue.append(node.left)
            
            # if the node right elements append it to the queue
            if node.right:
                queue.append(node.right)

        # return the root
        return root