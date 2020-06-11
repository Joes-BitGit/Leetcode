# # DESCRIPTION
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# EXAMPLE 1:
# Input: [3,2,3]
# Output: 3

# EXAMPLE 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    '''
    Time: O(N), must iterate over the array at least once
    Space: O(N), space for the hashmap which will have at most N - N/2 unique numbers
    '''

    def majorityElement(self, nums: List[int]) -> int:

        counts = {}
        # find the len/2
        majority = 0 + (len(nums) - 0) // 2

        for i in nums:
            # fill the hashtable counting each occurence of the int
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

            # when the majority is found return the current key
            if counts[i] > majority:
                return i
