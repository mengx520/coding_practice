'''
https://leetcode.com/problems/binary-search/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        - initialise two pointers left and right left = 0, rgiht = n - 1
        - while left <= right:
            - compare middle element of the array nums[middle] with target value
                - if target = nums[middle]: return middle
                - if target is not yet found:
                    - if target < nums[middle], search on the left, update right = middle - 1
                    - else target > nums[middle], search on the right, update left = middle + 1
        '''
        
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if target < nums[middle] :
                right = middle - 1
            else:
                left = middle + 1
        return -1