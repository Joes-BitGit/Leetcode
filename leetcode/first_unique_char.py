# DESCRIPTION
# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.

# EXAMPLE 1:
# s = "leetcode"
# return 0.

# EXAMPLE 2:
# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Time: O(N), only need to loop through the string twice
        Space: O(1), the hashtable can't grow larger than 26 letters
        '''
        first_unique = {}

        # fill hashtable
        for i in s:
            if i in first_unique:
                first_unique[i] += 1
            else:
                first_unique[i] = 1

        # iterate over the string again to check in the hashtable
        # need to look for the only unique char
        for i in range(len(s)):
            if first_unique[s[i]] == 1:
                return i

        # if we read the entire string and not found
        return -1
