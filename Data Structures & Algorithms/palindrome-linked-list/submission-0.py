# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_pointer = slow.next
            slow.next = prev

            prev, slow = slow, next_pointer
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            left, right = left.next, right.next
        return True
