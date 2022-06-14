'''
Time complexity Olog(N)
similar to 215.kth largest element
'''

import random
from collections import Counter

class Solution:
    def findKLargest(self, counts, k):
        pivot = random.choice(counts)
        left = [c for c in counts if c[1] > pivot[1]]
        mid = [c for c in counts if c[1] == pivot[1]]
        right = [c for c in counts if c[1] < pivot[1]]
        
        L, M = len(left), len(mid)
        
        if k < L:
            return self.findKLargest(left, k)
        elif k > L + M:
            return left + mid + self.findKLargest(right, k - (L + M))
        else:
            return left + mid[:k-L]
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(Counter(nums).items())

        largests = self.findKLargest(counts, k)
        
        return [l[0] for l in largests]