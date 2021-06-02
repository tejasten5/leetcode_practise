class Solution:
    roman_dict = {
            'I':1,'V': 5,'X':10,'L': 50,
            'C':100,'D':500,'M':1000, }        
    def romanToInt(self, s: str) -> int:                
        total = self.roman_dict[s[-1]]        
        for i in range(len(s)-1):  
            total = total - self.roman_dict[s[i]]  if self.roman_dict[s[i]] < self.roman_dict[s[i+1]] else total + self.roman_dict[s[i]]               
        return total
    
    def while_loop(self,s):
        print(len(s))
        i = 0
        #  == , < , > ,>=, <=
        while( i < len(s)):
            if  self.roman_dict[s[i]] <  self.roman_dict[s[i + 1]]:
                print('--')
            else:
                print(i,'++')

            i += 1



s = Solution()
# print(s.romanToInt("III"))
# print(s.romanToInt("IV"))
# print(s.romanToInt("IX"))
# print(s.romanToInt("LVIII"))
# print(s.romanToInt("MCMXCIV"))

# print(s.while_loop("LVIII"))