class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        1. initialize 2 integer variables, and set them both equal to first value of the array
        2. iterate through the array from the 2nd element. For each number, add it to the currentSubarray.
        if currentSubarray becomes negtive, it is not worth keeping, we throw it away. Then update maxSubarray everytime we 
        find new maxium
        3. return maxSubarray
        
        Time complexity: O(N)
        Space complexity: O(1)O

        '''
        # initialize current and max using first element
        current_sub = max_sub = nums[0]
        
        # iterate from the 2nd num
        for i in nums[1:]:
            # if current subarray is negtive, we throw it out, otherwise we add it to the current
            current_sub = max(current_sub + i, i)
            max_sub = max(current_sub, max_sub)
        return max_sub