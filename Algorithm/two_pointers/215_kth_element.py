'''
time complexity Olog(N)
quick select

pick random element as pivot
initial 3 pointer: smaller, equal, and larger than pivot
compare each group size with k: 
    if k smaller or equal than larger group size >> kth largest must inside larger group
    elif k - larger group size smaller than equal group size, which means kth largest elements is in equal group, then first element of equal group is the result
    else kth largest element is in smaller group, repeat findKthlargest function, but kth element became k - large group size - equal group size because we narrowed it down to te small group.

reference from: https://github.com/wisdompeak/LeetCode/tree/master/Binary_Search/215.Kth-Largest-Element-in-an-Array
'''

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        1. sort array >> [1,2,2,3,3,4,5,5,6]
        2. the kth largest element is in the -(k-1)th index
        '''
        pivot = random.choice(nums)
        
        small = [s for s in nums if s < pivot]
        equal = [e for e in nums if e == pivot]
        large = [l for l in nums if l > pivot]
        
        
        if k <= len(large):
            # result is in large parts
            return self.findKthLargest(large, k)
        
        elif (k - len(large)) <= len(equal):
            # result is first element in equal
            return equal[0]
        else:
            # result in small parts
            return self.findKthLargest(small, k - len(large) - len(equal))
