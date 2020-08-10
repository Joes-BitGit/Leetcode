# DESCRIPTION
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
# calculate the number of 1's in their binary representation and return them as an array.

# EXAMPLE 1:
# Input: 2
# Output: [0,1,1]

# EXAMPLE 2:
# Input: 5
# Output: [0,1,1,2,1,2]

# Follow up:
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss?
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution:
    '''
    Time: O(N), N is the given num
    Space: O(N), for the dp array to store the bits grows as the input grows
    '''

    def countBits(self, num: int) -> List[int]:
        dp = [0 for _ in range(num+1)]
        # offset will help us reset the bits to 1
        # this is necessary at: 2,4,8,16,32, etc
        offset = 1

        for i in range(1, num+1):
            # eg if 2 == 1*2
            # then a new bit has been added
            # so we must offset the index
            if i == offset*2:
                # offset -> 1, 2, 4, 8, 16, 32 etc.
                offset *= 2

            dp[i] = dp[i - offset] + 1

        return dp
