# DESCRIPTION
# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

# EXAMPLE 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# EXAMPLE 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

class Solution:
    '''
    Time: O(LOG N), Modified binary search
    Space: O(1)
    '''

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums)-1

        while l < r:
            mid = l + (r-l)//2
            parity = mid % 2

            # mid is even
            if parity == 0:
                if nums[mid] == nums[mid+1]:
                    # search right
                    l = mid+2
                else:
                    # search left
                    r = mid
            # mid is odd
            else:
                if nums[mid] == nums[mid+1]:
                    # search left
                    r = mid
                else:
                    # search right
                    l = mid+1

        # l should always be at the start of a pair
        return nums[l]
