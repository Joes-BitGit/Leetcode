# DESCRIPTION
# Write a function that reverses a string.
# The input string is given as an array of characters char[].

# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# EXAMPLE 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# EXAMPLE 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution:
    '''
    Time: O(N), where N is the length of the given string s
    Space: O(1), no auxiliary memory used + done in-place
    '''

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()

        # Try it with a two pointer approach
        left = 0
        right = len(s) - 1

        while left < right:
            # dont need to worry about odd/even
            # because the ptrs will cross past the odd since the middle
            # letter wont need to be reversed
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
