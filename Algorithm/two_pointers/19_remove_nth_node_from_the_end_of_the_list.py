'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        essentially the previous nodes of the removed nodes and current nodes has nth steps distance
        
        1. set two pointers at the beginning as head
        2. move first pointer n steps ahead
        3. check edge case if n == len(list) return head.next
        4. step both pointer forward until current nodes reach to the ends
        5. link previous nodes to the nodes after the removed nodes
        time complexity O(n)
        '''
        prev = current = head
        
        for i in range(n):
            current = current.next
        
        if current is None:
            return head.next
          
        while current.next:
            current = current.next
            prev = prev.next
        prev.next = prev.next.next
        
        return head