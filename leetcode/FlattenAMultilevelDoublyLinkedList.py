"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from collections import deque
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = deque()
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                

            else:
                if not curr.next and stack:
                    nxt = stack.pop()
                    curr.next = nxt
                    nxt.prev = curr
                
                curr = curr.next
                

        return head