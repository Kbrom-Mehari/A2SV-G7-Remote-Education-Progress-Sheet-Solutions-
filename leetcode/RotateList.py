# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        new_head = head
        new_tail = head
        tail = head

        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        if l != 0:
            k = k % l
        i = 0
        curr = head
        while curr:
            if i == l - k:
                new_head = curr
            if i == l - k - 1:
                new_tail = curr
            if i == l - 1:
                tail = curr
            i += 1
            curr = curr.next
        
        dummy.next = new_head
        if tail:
            tail.next = head
        if new_tail:
            new_tail.next = None

        return dummy.next
        

        