# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# EXAMPLE
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Time: O(N), worst case no 0s have to iterate over the entire array
        Space: O(1)
        '''
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 pointers
        # non zero ptr
        n = 0
        # array ptr
        a = 0

        """
        Mistake was using the i as the other pointer
        should be its own pointer as in
        """

        # iterate over the array
        for i in range(len(nums)):
            # if the non zero ptr is pointing at a non zero number
            if nums[n] != 0:
                # swap nonzero and array ptr
                nums[n], nums[a] = nums[a], nums[n]
                # inc nonzero ptr
                n += 1
                # inc array ptr
                a += 1
            # nonzero ptr is pointing at zero number
            else:
                # inc the non zero ptr
                n += 1
