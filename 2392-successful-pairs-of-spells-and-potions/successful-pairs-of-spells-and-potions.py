class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        x = []
        for i in spells:
            l,r,ans = 0,len(potions)-1,0
            while l<=r:
                m = (l+r)//2
                if (potions[m]*i)>=success:
                    ans+=(r-m+1)
                    r=m-1
                else: l=m+1
            x.append(ans);
        return x
        