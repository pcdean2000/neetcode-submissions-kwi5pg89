# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _push_left(node):
            while node:
                stack.append(node)
                node = node.left
        
        stack = []
        cur_val = -float(math.inf)
        _push_left(root)
        while stack:
            node = stack.pop()
            if not cur_val < node.val:
                return False
            cur_val = node.val
            _push_left(node.right)
        return True
