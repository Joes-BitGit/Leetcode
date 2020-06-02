# DESCRIPTION
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order of the remaining characters.
# (eg, "ace" is a subsequence of "abcde" while "aec" is not).
# A common subsequence of two strings is a subsequence that is common to both strings.
# If there is no common subsequence, return 0.

# EXAMPLE 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# EXAMPLE 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# EXAMPLE 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Time: O(N*M), where N is length of text1, M is the length of text2
        Space: O(N*M), 2D array needed of rows N and columns M
        '''
        # Dynamic Programming
        n = len(text1)
        m = len(text2)
        # includes empty string
        lcs = [[0 for i in range(m+1)] for j in range(n+1)]

        # fill table
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    lcs[i+1][j+1] = 1 + lcs[i][j]
                else:
                    lcs[i+1][j+1] = max(lcs[i+1][j], lcs[i][j+1])

        return lcs[-1][-1]
