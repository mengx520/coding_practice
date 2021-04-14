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



