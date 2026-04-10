# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        output = []
        n = 0
        
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        original_size = n // k

        extras = n % k
        curr = head
        for i in range(k):
            curr_head = curr
            size = original_size + (1 if i < extras else 0)
            
            for _ in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
            
            output.append(curr_head)
        
        return output