# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        stack = [(p, q)]
        while stack:
            np, nq = stack.pop()
            if not np or not nq or np.val != nq.val:
                return False
            if np.left or nq.left:
                stack.append((np.left, nq.left))
            if np.right or nq.right:
                stack.append((np.right, nq.right))
        return True