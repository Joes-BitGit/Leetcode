# DESCRIPTION
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# EXAMPLE 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# EXAMPLE 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
# which makes it impossible to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Time: O(N), where N is the len of the nums list
        Space: O(1), no auxillary memory used
        '''
        N = len(nums) - 1
        # start from the last index
        last_good_index = N

        # iterate backward
        for i in range(N, -1, -1):
            # curr_index + curr_value can reach the last position
            # that is known to reach the end
            if i + nums[i] >= last_good_index:
                last_good_index = i

        # the last good index should be the first index
        return last_good_index == 0
