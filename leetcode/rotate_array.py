class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        split = len(nums) - k
        nums[:] = nums[split:] + nums[:split]
