'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

time complexity O(N)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = {}
        left = 0
        
        '''
        seen stores the most current index of the characters that was last seen
        if right pointer index was not in seen(means not repeated yet), keep exdend window size by increase
        right pointer
        ''' 
        for right in range(len(s)):
            if s[right] not in seen:
                # longest substring size will be the window size
                result = max(result, right - left + 1)
                
            
            # if right pointer index was in seen there will be two cases:
            
            # case 1: right index was not inside current window, we can keep extending the window to the right
            # for example: abcfdbeaza ---> cdbeaz (a is in seen, but a is not in current because seen index of a is smaller than current a index, so we can keep extend until next condition hit)
            
            # case 2: if right index was inside the current window, we need to slide left pointer pass to the repeated index 
            # for example: abcfdbeaza --> cfdbeaz (b is inside current window, we need to update left pointer to c)
            
            
            else:
                if seen[s[right]] < left:
                    result = max(result, right - left + 1)
                else:
                    left = seen[s[right]] + 1
                    
            # we need to keep updaing the most current index of the characters
            seen[s[right]] = right
        return result
                
        

                            
                            

        