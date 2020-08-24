# DESCRIPTION
# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time: O(N), N because each node must be visited once to be swapped
    Space: O(N), recursion depth will at worst be the height of the tree 
                 which can be all the nodes
    '''

    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return

        right = root.right
        left = root.left
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)

        return root
