class Solution:
    def fun(self,x):
        temp = 0
        while (x > 0):
            r = x % 10
            temp = (temp * 10) + r
            x = x // 10          
        
        if temp in range(-2147483648 ,2147483648):            
            return temp
        else:
            return 0

    
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            x= x  * -1
            return self.fun(x) * -1
        if x > 0:
            return self.fun(x)


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))