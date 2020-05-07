# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process:
# Starting with any positive integer,
# replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.

# EXAMPLE
# Input: 19
# Output: true

# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Time: O(N LOG N), the inner loop iterations the length of N and we do that until we find 1 (N)
        Space: O(N), dictionary increases every iteration
        '''
        # Hashtable
        seen = {}

        # Iterate until we find 1
        while n != 1:
            # current value (temp)
            current = n

            # clear sum
            sum = 0

            # Generate the sum
            while current != 0:
                sum += (current % 10) ** 2
                current //= 10

            # Check the hashtable to see if we have already seen the sum
            # if seen already we are looping and the number is not happy
            if sum in seen:
                return False

            # add to the hashtable
            seen[sum] = 1
            n = sum

        return True
