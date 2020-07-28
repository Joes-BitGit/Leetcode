# DESCRIPTION
# We write the integers of A and B (in the order they are given)
# on two separate horizontal lines.

# Now, we may draw connecting lines:
# a straight line connecting two numbers A[i] and B[j] such that:

# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints:
# each number can only belong to one connecting line.

# Return the MAXIMUM number of connecting lines we can draw in this way.

# EXAMPLE 1:
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

# EXAMPLE 2:
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3

# EXAMPLE 3:
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2


# Note:
# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000

class Solution:
    '''
    Time; O(A*B), Must use a double for loop to iterate over the two arrays and compare
    Space: O(A*B), space needed for the dp array
    '''

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # edge cases
        if not A or not B:
            return None

        a_len = len(A)
        b_len = len(B)

        dp = [[0 for j in range(a_len + 1)] for i in range(b_len+1)]

        result = float('-inf')

        for i in range(1, b_len+1):
            for j in range(1, a_len+1):
                if B[i-1] == A[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                result = max(result, dp[i][j])

        return result
