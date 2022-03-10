'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        iterate negtive part in reverse way, and positive part forward way
        use two pointer to read positive and negative parts of the array
        one pointer j in the positive direction, another i in the negative direction
        time complexity O(N)
        '''
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        
        # i read in reserve way
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                temp_nums = nums[right]
                # iterate reverse way
                right -= 1
            else:
                temp_nums = nums[left]
                # iterate forward way
                left += 1
            result[i] = temp_nums * temp_nums  
        return result