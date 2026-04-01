# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_local_path_sum):
            if not node:
                return float("-inf"), max_local_path_sum
            left_path_sum, max_local_left_path_sum = dfs(node.left, max_local_path_sum)
            right_path_sum, max_local_right_path_sum = dfs(node.right, max_local_path_sum)
            max_local_path_sum = max(
                node.val,
                max_local_path_sum,
                max_local_left_path_sum,
                max_local_right_path_sum,
                left_path_sum,
                right_path_sum,
                left_path_sum + node.val + right_path_sum
            )
            return max(
                node.val,
                left_path_sum + node.val,
                right_path_sum + node.val
            ), max_local_path_sum
        return max(dfs(root, float("-inf")))
