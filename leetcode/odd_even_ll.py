# DESCRIPTION
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity
# and O(nodes) time complexity.

# EXAMPLE 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# EXAMPLE 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL


# Constraints:

# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# The length of the linked list is between [0, 10^4].
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Time: O(N), where N is the number of nodes in list
    Space: O(1), no extra data structure used
    '''

    def oddEvenList(self, head: ListNode) -> ListNode:
        # iterate over the og list
        # take the even positioned and place it in the new linked list
        # dont forget to reconnect nodes in the og list
        # finally append to the new ll to the og ll
        if head == None:
            return None

        # head doesnt move
        odd = head

        # e_head will point only to the even index nodes
        e_head = odd.next
        even = e_head

        # use even pointer as it closer to the end by 1 node
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # connects the odd index list to the even index list
        odd.next = e_head

        return head
