# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        if current:
            next_node = current.next
        while current and current.next:
            next_node = current.next
            if next_node.val == val:
                current.next = next_node.next
            #only we move current node if only next_node.val != val
            else:
                current = current.next           

        return dummy.next
        
            
        