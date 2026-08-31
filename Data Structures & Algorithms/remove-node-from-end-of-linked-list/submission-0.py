# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        prev, node = None, head
        for i in range(length - n):
            prev, node = node, node.next
        
        if node == head:
            return node.next
        elif node.next == None:
            prev.next = None
        else:
            prev.next = node.next 
        
        return head

        
        