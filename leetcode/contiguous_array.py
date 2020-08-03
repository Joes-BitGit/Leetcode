# DESCRIPTION
# Given a binary array, find the maximum length of a contiguous subarray
# with equal number of 0 and 1.

# EXAMPLE 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# EXAMPLE 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.

class Solution:
    '''
    Time: O(N), where N is the len of the given array, must iterate over the array at least once
    Space: O(N), space needed for the hashmap of the counts
    '''

    def findMaxLength(self, nums: List[int]) -> int:
        # hashtable to put the size of count at each index
        counts = {}

        # intialize hashmap when their are no entries
        counts[0] = -1

        max_length = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count += -1

            if count in counts:
                # find the max between the current max
                # and curr index - originally seen index
                max_length = max(max_length, i - counts[count])
            else:
                # when the counter is not in the hashmap
                # create an entry
                counts[count] = i

        return max_length
