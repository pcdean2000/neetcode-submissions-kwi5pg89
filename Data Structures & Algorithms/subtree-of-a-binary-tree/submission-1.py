# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def get_inorder(node):
            inorder_list = []
            stack = [node]
            while stack:
                node = stack.pop()
                if not node:
                    inorder_list.append("N")
                    continue
                inorder_list.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            return "".join(inorder_list)
            
        inorder_root = get_inorder(root)
        inorder_subroot = get_inorder(subRoot)

        print("inorder_root:", inorder_root)
        print("inorder_subroot:", inorder_subroot)

        return inorder_subroot in inorder_root


