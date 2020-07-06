# DESCRIPTION
# Given a binary search tree, write a function kthSmallest
# to find the kth smallest element in it.

# EXAMPLE 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1

# EXAMPLE 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Follow up:
# What if the BST is modified (insert/delete operations)
# often and you need to find the kth smallest frequently?
# How would you optimize the kthSmallest routine?


# Constraints:
# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time: O(N), N is the number of nodes
    Space: O(N), N is the depth of the tree which can be all nodes 
    '''

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None

        pos_val = [0, 0]

        # inorder print for a BST will print smallest to largest
        self.inorder(root, pos_val, k)

        return pos_val[1]

    def inorder(self, node, pos_val, k):
        if not node:
            return

        self.inorder(node.left, pos_val, k)
        # counting to see which element is kth
        pos_val[0] += 1
        if pos_val[0] == k:
            pos_val[1] = node.val
            return

        self.inorder(node.right, pos_val, k)
