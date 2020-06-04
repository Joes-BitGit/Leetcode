# DESCRIPTION
# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes
# from some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

# EXAMPLE 1:
# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6

# EXAMPLE 2:
# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        Time: O(N), number of nodes iterated once
        Space: O(H), stack frames goes height level deep at most
        '''
        self.max_path_sum = float('-inf')
        self.path_sum(root)
        return self.max_path_sum

    def path_sum(self, node):
        if not node:
            return 0

        # doesn't return negatives
        left = max(0, self.path_sum(node.left))

        right = max(0, self.path_sum(node.right))

        # checks the triangle (left parent right) compares it to the global max
        # if its larger than our global then we have a path: left parent right
        self.max_path_sum = max(self.max_path_sum, left + right + node.val)

        # returns either the left track or the right track
        # can only choose one for the next level of the stack frame
        return max(left, right) + node.val
