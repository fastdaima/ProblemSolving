import sys 

from os import path 


def read_input(): 
    if path.exists("input.txt"): 
        read = open('input.txt', 'r').readline
        write = open('output.txt', 'w').write
    
    return read, write 

read, write = read_input()

def map_inp_var():
    return (tuple(map(int, read().split())))

def map_inp_arr():
    return list(map(int, read().split()))

w = int(read())


for _ in range(w): 
    n, l, r = map_inp_var()
    # print(n,l,r)
    a = map_inp_arr()
    a = sorted(a)

    start = 0 
    end = 0
    count = 0
    # print(a, '\t')

    while(start<n):
        n-=1
        while(start<n and a[start]+a[n]<l):
            start += 1
        while(end<n and a[end]+a[n]<=r):
            end += 1

        count += min(end, n) - start 
    # print(count)
    write(str(count)+'\n')

