# DESCRIPTION
# Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number is the smallest possible.
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

# EXAMPLE 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# EXAMPLE 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

# EXAMPLE 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

class Solution:
    '''
    Time: O(N), must iterate over the entire string 
    Space: O(N), size of the stack used grows as the input grows
    '''

    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        max_stack = len(num) - k

        # edge case
        if max_stack == 0:
            return '0'

        for i in num:
            # stack is not empty
            # the top element > curr
            # k has not been satisfied
            while stack and i < stack[-1] and k > 0:
                k -= 1
                stack.pop()

            stack.append(i)

        # if there are still digits to delete
        # remove the top one(s)
        if k > 0:
            stack = stack[:-k]

        # delete leading 0s if they exist
        return "".join(stack).lstrip("0") or '0'
