# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smalls = ListNode(-1)
        non_smalls = ListNode(-1)
        
        curr_small = smalls
        curr_non_small = non_smalls

        while head:
            if head.val < x:
                curr_small.next = head
                curr_small = curr_small.next
            else:
                curr_non_small.next = head
                curr_non_small = curr_non_small.next
            head = head.next
        
        curr_small.next = non_smalls.next
        curr_non_small.next = None

        return smalls.next