# DESCRIPTION
# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# EXAMPLE 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# EXAMPLE 2:
# Input: J = "z", S = "ZZ"
# Output: 0


class Solution:
    '''
    Time: O(J+S), J is the len of char array, S is len of char array
    Space: O(J), turns the array of jewels into set data structure
    '''

    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        # set saves on memory from dict
        jewels = set(J)

        for item in S:
            if item in jewels:
                counter += 1

        return counter
