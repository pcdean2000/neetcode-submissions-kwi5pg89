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
        print("encoded tree:", res)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # convert from inorder string
        def dfs(data_list):
            val = data_list.pop()
            print("val:", val)
            if val == "N":
                return None, data_list
            node = TreeNode(val)
            node.left, data_list = dfs(data_list)
            node.right, data_list = dfs(data_list)
            return node, data_list

        data_list = data.split(",")[::-1]
        root, _ = dfs(data_list)
        return root
