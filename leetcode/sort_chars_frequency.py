# DESCRIPTION
# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    '''
    Time: O(N LOG N), where N is the length of the string because must sort the dictionary 
    Space: O(N), space for hashtable of the chars in string
    '''

    def frequencySort(self, s: str) -> str:
        result = ''
        if not s or len(s) == 0:
            return result

        char_count = {}

        for i in s:
            char_count[i] = char_count.get(i, 0) + 1

        # sort the dictionary in descending order by value
        # key makes the dictionary get sorted by value, in this case letter count
        # reverse=True sorts in descending order largest to smallest
        sort_char_count = sorted(char_count, key=char_count.get, reverse=True)
        for char in sort_char_count:
            result += char_count[char] * char

        return result
