# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # convert to inorder string
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append("N")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # convert from inorder string
        data_list = data.split(",")[::-1]

        def dfs():
            val = data_list.pop()
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        root= dfs()
        return root
