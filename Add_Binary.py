class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        a = a.zfill(l)
        b = b.zfill(l)

        ans = []
        carry = 0
        for i in reversed(range(l)):
            r = carry

            if a[i] == '1':
                r += 1

            if b[i] == '1':
                r += 1

            if r == 0:
                ans.append(0)
                carry = 0
            elif r == 1:
                ans.append(1)
                carry = 0
            elif r == 2:
                ans.append(0)
                carry = 1
            elif r == 3:
                ans.append(1)
                carry = 1

        if carry == 1:
            ans.append(1)

            
            
            
        return ''.join(map(str, reversed(ans)))



        







s = Solution()
s.addBinary("11","1")
# print()