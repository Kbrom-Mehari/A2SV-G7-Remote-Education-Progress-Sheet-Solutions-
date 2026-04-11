# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        half = n // 2
        
        curr = head
        next_head = head
        for _ in range(half - 1):
            if curr:
                curr = curr.next
        next_head = curr.next
        curr.next = None

        
        prev = None
        curr = next_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        next_head = prev

        max_twin_sum = 0
        
            
        while head and next_head:
            twin_sum = head.val + next_head.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            head = head.next
            next_head = next_head.next
        
        return max_twin_sum