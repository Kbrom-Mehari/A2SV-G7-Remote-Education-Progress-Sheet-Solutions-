# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        prev_node = None
        
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = nxt
        
        tail = prev.next
        
        prev.next = prev_node
        tail.next = curr
        
        return dummy.next
        