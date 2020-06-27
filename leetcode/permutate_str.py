# DESCRIPTION
# Given two strings s1 and s2, write a function to return true
# if s2 contains the permutation of s1. In other words,
# one of the first string's permutations is the substring of the second string.


# EXAMPLE 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# EXAMPLE 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

# Constraints:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

class Solution:
    '''
    Time: O(N + M), N is the len of s1 and M is the len of s2
    Space: O(N), dictionary of size s1
    '''

    def checkInclusion(self, s1: str, s2: str) -> bool:
        N = len(s1)
        M = len(s2)

        if N > M:
            return False

        s1_dict = {}

        for c in s1:
            if c in s1_dict:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 1

        counter = len(s1_dict)
        left, right = 0, 0

        while right < M:
            char2 = s2[right]

            if char2 in s1_dict:
                s1_dict[char2] -= 1
                if s1_dict[char2] == 0:
                    counter -= 1
            right += 1

            while counter == 0:
                c = s2[left]

                if c in s1_dict:
                    s1_dict[c] += 1
                    if s1_dict[c] > 0:
                        counter += 1
                if right-left == N:
                    return True

                left += 1

        return False
