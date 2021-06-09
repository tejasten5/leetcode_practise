class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


s = "Hello how are you Contestant"
k = 4
s1 = Solution()
print(s1.truncateSentence(s,k))
