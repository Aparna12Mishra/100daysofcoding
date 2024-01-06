class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Total value of the nums
        tot = sum(nums)
        left = 0

        # Iterating through the list
        for index, ele in enumerate(nums):
            # Calculating the right side value
            right = tot - left - ele
            # Checking if both sides are equal
            if right == left:
                return index
            # Updating left side
            left += ele
        # No answers found, so...
        return -1