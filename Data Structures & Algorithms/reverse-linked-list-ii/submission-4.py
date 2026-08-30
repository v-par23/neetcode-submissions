# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        leftPrev, current_node = dummy_head, head

        for i in range(left -1):
            leftPrev, current_node = current_node, current_node.next
        
        prev = None 
        for i in range(right - left + 1):
            next_pointer = current_node.next
            current_node.next = prev
            prev, current_node = current_node, next_pointer
        
        leftPrev.next.next = current_node
        leftPrev.next = prev
        return dummy_head.next




