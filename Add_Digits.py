class Solution:
    def addDigits(self, num: int) -> int:
        
        while int(num) >= 10:
            num = sum([int(i) for i in str(num)])
            
        return num


    def constant_logic(self,num):
        num = int(num)
        if num == 0:
            return num
        if num % 9 == 0:
            return 9
        return num % 9



        

s = Solution()
print(s.constant_logic("38"))