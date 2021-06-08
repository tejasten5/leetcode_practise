class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        return  max(d,key = d.get)
    
    def linear_time(self,nums):
        nums.sort()
        return nums[len(nums) // 2]
        
s = Solution()
# print(s.majorityElement([3,2,3]))
print(s.linear_time([3,2,3,2,3,5,4,4,5,6,54,6,8,0,10,11]))