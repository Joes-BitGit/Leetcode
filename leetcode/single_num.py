class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Time: O(N), number of elements in nums array
        Space: 0(1), no extra space is needed
        '''
        # Bit manipulation
        # eg a ^ 0 = a
        # a ^ a = 0
        # a ^ b ^ b = a
        # the b's cancel out
        a = 0

        for i in nums:
            a ^= i

        return a
