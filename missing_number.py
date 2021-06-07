class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return [i for i in range(0,n) if i not in nums][0]
