

# s = s.split()
# c = {}
# for i,j in enumerate(s):
#     c[int(j[-1])] = j[:-1]
# print(c)
# print([c[i] for i in range(1, len(c)+1)])

def sortSentence(s) -> str:
    s = s.split(" ")
    result = [None] * len(s)

    for i in range(len(s)):
        
        result[int(s[i][-1]) - 1] = s[i][0:len(s[i]) - 1] 
        
    
    return " ".join(result)

sortSentence("is2 sentence4 This1 a3")