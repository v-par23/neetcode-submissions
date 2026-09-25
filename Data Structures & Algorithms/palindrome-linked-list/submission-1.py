# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle 
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reerse linked list from second half
        prev = None
        while slow:
            nextt = slow.next 
            slow.next = prev 

            prev = slow 
            slow = nextt

        #check palindfrom with to pointers
        left = head
        right = prev 
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next 

        return True 
