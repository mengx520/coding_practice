# Two Passes - Forward and Backward
# Time: O(n)
# Space: O(n)

class Solution:
	def longestMountain(self, arr: List[int]) -> int:
		up = [0]*len(arr)
		down = [0]*len(arr)
        
		for i in range(1, len(arr)):
			if arr[i] > arr[i-1]:
				up[i] = up[i-1]+1
                
		for i in range(len(arr)-1)[::-1]:
			if arr[i] > arr[i+1]:
				down[i] = down[i+1]+1
		res = 0
        
		for i, j in zip(up, down):
			if i and j:
				res = max(res, i+j+1)
		return res