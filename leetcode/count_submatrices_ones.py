# DESCRIPTION
# Given a m * n matrix of ones and zeros,
# return how many square submatrices have all ones.

# EXAMPLE 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# EXAMPLE 2:
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.


# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

class Solution:
    '''
    Time : O(m*n), m is rows and n is cols
    Space: O(m*n), dp array 
    '''

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        # counts the number of squares
        result = 0

        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == 0:
                    dp[i][j] = 0
                else:
                    square = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    dp[i][j] = square + 1
                result += dp[i][j]

        return result
