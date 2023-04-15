
import math
from collections import Counter

class Solution:
    '''Solution using dictionary'''
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = []
        hash_set = {}
        for o in cpdomains:
            number, domain = o.split(' ')
            number = int(number)
            subdomains = domain.split('.')
            len_subdomain = len(subdomains)
            start_index = 0
            while start_index < len_subdomain:
                domain_ = ".".join(subdomains[start_index:])
                # print(domain_)
                if domain_ in hash_set:
                    hash_set[domain_] += number
                else:
                    hash_set[domain_] = number
                start_index += 1

        for k,v in hash_set.items():
            output.append(f'{v} {k}')
        return output

## Solution 2 ########################
class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

    def ins(self, list_, idx, count):
        print('***********************************INSERT')
        self.count += count
        if idx == len(list_): return

        if list_[idx] not in self.children:
            self.children[list_[idx]] = Node()
        self.children[list_[idx]].ins(list_, idx+1, count)
        print(idx, list_, self.children[list_[idx]])
        print()
        print()

    def trav(self, ret, prefix):
        print('***********************************')
        print('in traversal')
        print(self.count, prefix)
        ret.append((self.count, prefix))
        for ch in self.children:
            self.children[ch].trav(ret, ch+"."+prefix)
        print()
        print()


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        '''using trie'''
        root = Node()

        for input in cpdomains:
            count, d = input.split(' ')
            count = int(count)
            d = d.split('.')[::-1]
            print(f'domains {d}')
            root.ins(d, 0, count)

        ret = []
        root.trav(ret, '')
        ans = []

        for x, y in ret:
            if y=='': continue
            ans.append(f'{x} {y[:-1]}')
        return ans




