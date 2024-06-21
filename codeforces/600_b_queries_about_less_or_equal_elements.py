
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = sorted(a)


def binary_search(a, target): 
    start = 0 
    end = len(a)-1

    while start <= end: 
        mid = (start+end)//2
        if start==end: break
        
        if a[mid]<=target:
            start = mid+1 
        else: 
            end = mid
    
    if a[mid]<=target: 
        return mid+1 
    
    return mid 


out = []

for o in b: 
    print(binary_search(a, o), end=' ')

