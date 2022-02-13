// https://leetcode.com/problems/reverse-linked-list

import queue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node=head
        q=queue.Queue()
        q.put(None)
        while cur_node:
            q.put(cur_node.next)
            cur_node.next=q.get()
            q.put(cur_node)
            cur_node=q.get()
            
        return q.get()    