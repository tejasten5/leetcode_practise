class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        else:
            li = s.split()
            return len(li[-1])

s = Solution()               
print(s.lengthOfLastWord())