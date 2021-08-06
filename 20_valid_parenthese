'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
https://leetcode.com/problems/valid-parentheses/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []