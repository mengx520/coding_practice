
'''
sort the two list, and use two pointer to search in the lists to find common elements.
O(nlogn + mlogm) Time and O(1) Space.
''' 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
		            """ 
								If the result list is empty or the last thing we added wasn't this element, 
								then it's a new element we need to add
								"""
                if len(res) == 0 or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res
