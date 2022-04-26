class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        the search function is to find the lowest index of target in nums. 
        since nums are sorted in non decreasing order 
        search(target+1) means the very next index of the largest index of target in nums. 
        and to return the target index search(target+1) -1
        time complexity olog(n)
        '''
        def search(x):
            left, right = 0, len(nums) 
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < x:
                    left = middle + 1
                else:
                    right = middle
            return left
        
        left = search(target)
        right = search(target + 1) - 1
        
        if left <= right:
            return [left, right]
        
        else:
            return [-1, -1]