class Solution:
    def calPoints(self, ops: List[str]) -> int:
        r = []
        for i in ops:
            try:
                i = int(i)
            except:
                i = i
            if isinstance(i,int):
                r.append(int(i))
            elif i == "D":
                r.append(r[len(r) - 1] * 2)
            elif i == "C":
                r.remove(r[len(r) - 1])
            elif i == "+":
                r.append(r[len(r) - 2] + r[len(r) - 1])
            print(r,'AA')
        print(r)
        return sum(r)
                
        
