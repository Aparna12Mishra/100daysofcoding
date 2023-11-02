class Solution:
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.helper(root, ans)
        return ans[0]
        
    def sum(self, root, arr):
        if root is None:
            return
        arr[0] += root.val
        arr[1] += 1

        self.sum(root.left, arr)
        self.sum(root.right, arr)

    def helper(self, root, ans):
        if root is None:
            return

        arr = [0, 0]
        self.sum(root, arr)
        avg = arr[0] // arr[1]

        if root.val == avg:
            ans[0] += 1

        self.helper(root.left, ans)
        self.helper(root.right, ans)