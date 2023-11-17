class Solution:
    def minPairSum(self, nums):
      
        nums.sort()
        n = len(nums)

        i, j = 0, n - 1
        maxi = float('-inf')

       
        while i < j:
            pair_sum = nums[i] + nums[j]
          
            maxi = max(pair_sum, maxi)
            i += 1
            j -= 1
        
      
        return maxi

