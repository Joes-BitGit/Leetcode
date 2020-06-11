# DESCRIPTION
# In a binary tree, the root node is at depth 0,
# and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth,
# but have different parents.
# We are given the root of a binary tree with unique values,
# and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# EXAMPLE 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# EXAMPLE 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# EXAMPLE 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time: O(N), where N is the number of nodes
    Space: O(N), where N is the stack frames of the dfs, 
           this is the worst case when the tree only goes down one side
    '''

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Assumption: there are only unique elements in the tree

        # Tells us who the parents are of the current node
        self.parent_x = None
        self.parent_y = None

        # Tells us the depth of the current node
        self.level_x = -1
        self.level_y = -1

        self.dfs(root, None, 0, x, y)

        # parents must be different
        not_siblings = self.parent_x != self.parent_y

        # depth must be the same
        level = self.level_x == self.level_y

        return not_siblings and level

    def dfs(self, node, parent, depth, x, y):
        # stop when there are no more nodes
        if not node:
            return
        else:
            # if x or y is the value we are searching for
            # then update parent and depth
            if node.val == x:
                self.parent_x = parent
                self.level_x = depth

            if node.val == y:
                self.parent_y = parent
                self.level_y = depth

            self.dfs(node.left, node, depth+1, x, y)
            self.dfs(node.right, node, depth+1, x, y)
