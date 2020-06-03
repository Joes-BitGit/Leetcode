# DESCRIPTION
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.

# EXAMPLE:
# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Time: O(N*M), where N is the width of the matrix, M is the height of the matrix
        Space: O(N*M), space for the DP array 
        '''
        if not matrix:
            return 0

        width = len(matrix[0]) + 1
        height = len(matrix) + 1
        dp = [[0 for i in range(width)] for _ in range(height)]

        # side of the largest square
        result = 0

        for i in range(height-1):
            for j in range(width-1):
                # no possible square
                if matrix[i][j] == "0":
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i][j+1], dp[i+1][j])

                # is the prev best square larger or the new square
                result = max(result, dp[i+1][j+1])

        # need to multiple it with itself since we only return the length
        # of one side
        return result**2
