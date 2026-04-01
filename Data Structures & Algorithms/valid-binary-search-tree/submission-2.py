# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, l_bound, r_bound):
            if not node:
                return True
            if not l_bound < node.val < r_bound:
                return False
            return (validate(node.left, l_bound, node.val) and
                    validate(node.right, node.val, r_bound))
                
        return validate(root, -1001, 1001)
