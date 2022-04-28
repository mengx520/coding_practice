'''
time complexity olog(n)
worst o(N)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right=0, len(nums)-1

        while(left <= right):

            # shifting to remove duplicate elements
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            # step 1 calculate the mid    
            mid = (left + right) // 2

            #step 2
            if nums[mid] == target:
                return True

            #step 3
            elif nums[left] <= nums[mid]:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid-1
                else:
                    left = mid+1

            # step 4
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        # step 5
        return False