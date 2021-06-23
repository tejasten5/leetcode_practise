s = ["H","a","n","n","a","h"]
left,right = 0,len(s) - 1
while left < right:
    print(s[left],s[right])
    s[left],s[right] = s[right],s[left]
    left,right = left+1,right - 1
