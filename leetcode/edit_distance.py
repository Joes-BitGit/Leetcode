# DESCRIPTION

# Given two words word1 and word2,
# find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# EXAMPLE 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# EXAMPLE 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    '''
    Time: O(M*N), M is the length of word 1, N is the length of word 2
    Space: O(M*N), Space for the dp array
    '''

    def minDistance(self, word1: str, word2: str) -> int:
        w1_len = len(word1)
        w2_len = len(word2)

        dp = [[i+j for j in range(w1_len+1)] for i in range(w2_len+1)]

        '''
        fill the dp array
            if the chars are the same no extra op is needed,
            take dp[i-1][j-1] place it in dp[i][j]
            else:
            take the min of surrounding + 1
        return dp[-1][-1]
        '''

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if word2[i-1] != word1[j-1]:
                    # they are different
                    # we need to find out which operation takes the least amount of work
                    # +1 is needed for the replacement of the curr char since they are different
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    # they are equal
                    # the answer to the subproblem is the answer of the len-1 of each string
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]
