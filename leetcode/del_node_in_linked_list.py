# DESCRIPTION
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.

# Given linked list -- head = [4,5,1,9]

# EXAMPLE 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5,
# the linked list should become 4 -> 1 -> 9 after calling your function.

# EXAMPLE 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1,
# the linked list should become 4 -> 5 -> 9 after calling your function.


# Note:
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Time: O(1), constant time because we are only reassigning values
    Space: O(1), constant space no auxillary memory used
    '''

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Replaces the current value with the next value
        node.val = node.next.val
        # the current node then skips over the next node to point to the one after
        node.next = node.next.next
