# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(curr, nxt, last):

            if last:
                curr.next = nxt.next
                last.next = nxt
                nxt.next = curr
                last = curr
            else:
                curr.next = nxt.next
                nxt.next = curr
                last = curr
            
            return last
        

        if head and head.next:
            future_head = head.next
        else:
            return head
        

        curr = head
        last = None
        while curr and curr.next:
            last = swap(curr, curr.next, last)
            curr = curr.next


        return future_head