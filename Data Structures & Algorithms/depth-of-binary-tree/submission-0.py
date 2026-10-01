# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BINARY TREE NODE CHEAT SHEET
# node.val → current node's value
# node.left → left child
# node.right → right child
# if node → check if current node exists
# if not node → current node is None
# if node.left → check if left child exists
# if node.right → check if right child exists
# if not node.left and not node.right → current node is a leaf
# node.left = new_node → set/change the left child
# node.right = new_node → set/change the right child
# node.val = value → set/change the node's value
# TreeNode(val, left, right) → common tree node structure
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            return 1 + max(left, right)
        
        return dfs(root)



        