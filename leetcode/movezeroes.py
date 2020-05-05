class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # iterates through entire list
        curr = 0

        # only iterates through non-zero values
        ptr = 0

        for i in range(len(nums)):
            if nums[ptr] != 0:
                nums[ptr], nums[curr] = nums[curr], nums[ptr]
                ptr += 1
                curr += 1
            else:
                ptr += 1
