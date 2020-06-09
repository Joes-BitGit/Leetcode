# DESCRIPTION
# Given a positive integer num, output its complement number.
# The complement strategy is to flip the bits of its binary representation.

# EXAMPLE 1:
# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.

# EXAMPLE 2:
# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits),
# and its complement is 0. So you need to output 0.

class Solution:
    '''
    Time; O(N), where N is the length of number in bits
    Space: O(1)
    '''

    def findComplement(self, num: int) -> int:
        # e.g 101 XOR 2^bit_length-1
        # 2^bit_length(num) = 8 -> 1000
        # 8-1 = 7 -> 111
        # 5:101 ^ 7:111 = 010 -> 2
        num_bits = num
        count = 0
        if num_bits == 0:
            return 1

        while num_bits != 0:
            num_bits >>= 1
            count += 1

        # return num ^ 2 ** (len(bin(num))-2)-1
        # return num ^ 2 ** num.bit_length() - 1
        return num ^ 2 ** count - 1


# obj = Solution()
# print(obj.findComplement(5))
