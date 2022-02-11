// https://leetcode.com/problems/delete-node-in-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmp_val = node.next.val
        tmp_next = node.next.next
        node.val = tmp_val
        node.next = tmp_next
        