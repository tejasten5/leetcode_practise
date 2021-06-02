"""
without converting to str.
"""
class Solution:
    def isPalindrome(self,x):
        isPalin = False
        temp = 0

        n = x

        if x < 0 :
            return False

        while x != 0:
            rem = x % 10
            temp = (temp * 10) + rem
            x = x // 10
        return True if temp == n else False

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))