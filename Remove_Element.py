class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        li = []
        for k in nums:            
            if k != val:
                li.append(k)           
        print(li)
        return len(li)
        


# 3
# [0,1,2,2,3,0,4,2],2
s = Solution()
s.removeElement([3,2,2,3],3)