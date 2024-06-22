import sys 

from os import path 


def read_input(): 
    if path.exists("input.txt"): 
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'r')
    
    input_ = sys.stdin.readline()
    return input_



breakpoint()
w = read_input() 


# sys.stdout.close()