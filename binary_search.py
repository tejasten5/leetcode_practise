li = [-1,0,3,5,9,12]
target = 9

def binary_search(List,target):
    low,high = 0,len(List) - 1
    
    while(low <= high):
        mid = (low+high)//2
        
        if List[mid] == target:
            return mid
        else:
            if List[mid] < target :
                low = mid + 1
            else:
                high = mid - 1
    return -1


r = binary_search(li,target)
print(r)