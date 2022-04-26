# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader, target):
        left, right = 0, 10001
        while left <= right:
            middle = (left + right) // 2
            ans = reader.get(middle)
            if ans == target: 
                return middle
            elif ans < target:
                left = middle + 1
            else: 
                right = middle - 1
        return -1