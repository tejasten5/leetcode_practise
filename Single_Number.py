class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        context = {}
        if len(nums) <= 1:
            return nums[0]
            
        for i in range(len(nums)):
            if nums[i] in context:
                context[nums[i]] += 1
            else:
                context[nums[i]] = 1
        
        for k,v in context.items():
            if v == 1:
                return k


s = Solution()
print(s.singleNumber([4,1,2,1,2]))
        