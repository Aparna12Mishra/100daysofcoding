class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [num * num for num in nums]
        squares.sort()
        return squares