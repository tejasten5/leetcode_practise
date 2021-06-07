class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        li = ['b','a','l','o','n']
        context = {}
        for i in text:
            print(i)
            if i in li:
                context[i] += 1
            else:
                context[i] = 1
        print(context)
                


s = Solution()
print(s.maxNumberOfBalloons("oonbalxballpoon"))