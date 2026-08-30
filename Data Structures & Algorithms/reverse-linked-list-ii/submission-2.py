# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        leftPrev, curr = dummy_head, head

        for i in range(left -1):
            leftPrev, curr = curr, curr.next
        
        prev = None 
        for i in range(right - left + 1):
            next_pointer = curr.next
            curr.next = prev
            prev, curr = curr, next_pointer
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy_head.next




