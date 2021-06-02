class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))      
        
        nums.sort()
        return max(nums) if len(nums) <= 2 else nums[-3]


s = Solution()
print(s.thirdMax([3,2,1]))