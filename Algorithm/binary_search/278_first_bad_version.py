'''
https://leetcode.com/problems/first-bad-version/
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''
This is essentially a finding first change in the array problem
The change condition is after finding the change, all the right index of the array are changed, yet on the left side of the change still could have change
Goal is to find when the change began
Same binary search consept
- Divide the array in the middle
    - if middle is not the change, new left begins from middle + 1, until left and right become equal
    - if middle is the change, chop off the right, middle become the new right

Time complexity Olog(N)'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            middle = left + (right - left) // 2 
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1    
        return left