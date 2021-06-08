class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for i in digits:
            s += str(i)
        t = eval(s) +1
        
        return list(str(t))


s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))