'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        1. convert input string to array and create empty list
        2. loop through array
        3. reverse each word
        4. change string back to array
        5. add to ans list
        6. add space and convert back to string
        time complexity O(N)
        '''
        
        arr = s.split()
        ans = []
        
        for w in arr:
            w = list(w)
            left, right = 0, len(w) - 1
            while left < right:
                w[left], w[right] = w[right], w[left]
                left, right = left + 1, right - 1
            new_order = ''.join(w)
            ans.append(new_order)
        
        return (' '.join(ans))

            
        
           