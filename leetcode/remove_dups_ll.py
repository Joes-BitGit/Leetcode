# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head != None:
            ptr = head
            tail = head

            while ptr.next != None:
                if ptr.next.val == tail.val:
                    ptr.next = ptr.next.next
                    tail.next = ptr.next
                else:
                    tail = tail.next
                    ptr = ptr.next

        return head
