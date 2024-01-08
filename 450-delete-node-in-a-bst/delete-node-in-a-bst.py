# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.actual_node_found = None
        def find_val(node, key):
            if node == None:
                return node

            if node.val == key:
                if node.right and node.left:
                    self.actual_node_found = node
                if node.right:
                    return node.right
                else:
                    return node.left
                return None
            
            node.left = find_val(node.left, key)
            node.right = find_val(node.right, key)

            return node

        root = find_val(root, key)
        
        if self.actual_node_found is None or \
        self.actual_node_found.left is None:
            return root

        right = self.actual_node_found.right
        left = self.actual_node_found.left
        prev_node = right
        while True:
            prev = right
            if right.val > left.val:
                right = right.left
            else:
                right = right.right

            if right == None:
                break
        
        if prev.val > left.val:
            prev.left = left
        else:
            prev.right = left

        return root

