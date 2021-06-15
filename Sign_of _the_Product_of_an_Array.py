class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        nums = sum(map(lambda x:x<0,nums))
        if nums % 2 == 0:
            return 1
        return -1
            
        
