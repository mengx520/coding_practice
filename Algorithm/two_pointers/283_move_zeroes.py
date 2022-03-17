'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        set two pointer first, second    
        if second is not 0 swap with first
        first move forward
        time complexity O(n)
        '''
        
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
        