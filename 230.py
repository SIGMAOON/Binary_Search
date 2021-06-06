# Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        order = []
        
        def inorder(node):
            if node is None:
                pass
            else:
                inorder(node.left)
                order.append(node.val)
                inorder(node.right)
        
        inorder(root)
        
        return order[k-1]