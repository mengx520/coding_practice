'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        - initiate left, right = 0, len(nums) - 1
        - left < right
        - find middle index of the array left + (right - left) // 2
        - compare target with middle index
            - if target = nums[middle]:
                return middle
            - if target < nums[middle]:
                right = middle - 1
            - else:
                left = middle + 1
        return left
        
        time comlexity olog(n)
        '''
        
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return left