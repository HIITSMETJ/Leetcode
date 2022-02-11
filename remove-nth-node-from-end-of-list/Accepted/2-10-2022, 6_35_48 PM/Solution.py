// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=head
        sz=0
        idx={}
        while node:
            sz+=1
            idx[sz]=node
            node=node.next
            
        if sz-n>0:
            idx[sz-n].next=idx[sz-n+1].next
        elif sz>1:
            head=head.next
        else:
            head=None
        return head