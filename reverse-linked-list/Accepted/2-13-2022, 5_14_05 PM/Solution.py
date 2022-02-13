// https://leetcode.com/problems/reverse-linked-list

import queue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        elif head.next==None:
            return head
        else:
            tmp = head.next
            re=self.reverseList(head.next)
            tmp.next=head
            head.next=None
            return re
