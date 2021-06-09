class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

# sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
s = Solution()
print(s.checkIfPangram(sentence))