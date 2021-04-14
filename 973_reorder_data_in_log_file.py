'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
'''
'''
Example1
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit = []
        letter = []

        for i in logs:

            # check if new_list index 1 is digit
            if i.split()[1].isdigit():
                # update digit list
                digit.append(i)
            # check if new_list index 1 is letter
            else:
                # update letter list
                letter.append(i)
        
        letter.sort(key = lambda x: x.split()[0])
        letter.sort(key = lambda x: x.split()[1:])
        

        return letter + digit
        sorted_letter + 



