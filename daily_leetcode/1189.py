class Solution:
    'brute force'
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_dict = {}

        for char in text:
            if char in 'balon':
                if char in hash_dict:
                    hash_dict[char]+=1
                else:
                    hash_dict[char]=1

        if 'o' in hash_dict: hash_dict['o'] = hash_dict['o']//2
        if 'l' in hash_dict: hash_dict['l'] = hash_dict['l']//2

        return min(hash_dict.values())if(len(hash_dict)==len('balon')) else 0

import math
from collections import Counter
class Solution:
    '''optimised solution'''
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        mx = math.inf
        for t in 'balon':
            amt = 1 if t in 'ban' else 2
            mx = min(mx, c.get(t, 0) // amt)
        return mx