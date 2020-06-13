# DESCRIPTION
# Given a positive integer num, write a function which
# returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

# EXAMPLE 1:
# Input: num = 16
# Output: true

# EXAMPLE 2:
# Input: num = 14
# Output: false

class Solution:
    '''
    Time: O(log N), binary search algorithm
    Space: O(1), no extra data structure used and no stack frames
    '''

    def isPerfectSquare(self, num: int) -> bool:

        left = 0
        right = num

        while left <= right:
            # mid point while not overflowing
            # integer/floor division
            mid = left + (right - left) // 2

            # search the left side
            if mid**2 > num:
                right = mid - 1
            # search the right
            elif mid**2 < num:
                left = mid + 1
            # num found
            else:
                return True

        # no valid square
        return False
