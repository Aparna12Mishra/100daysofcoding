class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sm = [0]
        def cal(r,lvl):
            if len(sm)<lvl:
                sm.append(0)
            sm[lvl-1]+=r.val
            if r.right:
                cal(r.right,lvl+1)
            if r.left:
                cal(r.left,lvl+1)
        cal(root,1)
        mx=max(sm)
        for idx, x in enumerate(sm):
            if x == mx:
                return idx+1