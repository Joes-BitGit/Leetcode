# DESCRIPTION
# Given a string s and a non-empty string p,
# find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and
# the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# EXAMPLE 1:
# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# EXAMPLE 2:
# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    '''
    Time: O(NxM), N is the len of s, M is the len of p
    Space: O(M), space for the dictionary that has char p
    '''

    def findAnagrams(self, s: str, p: str) -> List[int]:

        result = []

        # edge case
        if len(p) > len(s) or len(p) == 0:
            return result

        # dictionary to hold counts of the string i am looking for
        p_map = {}

        # fills the dictionary with the counts of each char
        for c in p:
            if c in p_map:
                p_map[c] += 1
            else:
                p_map[c] = 1

        # size of dictionary not including duplicates
        counter = len(p_map)
        # 2 pointers to iterate over the strings
        left, right = 0, 0

        while right < len(s):
            if s[right] in p_map:
                p_map[s[right]] -= 1
                # if the right amount of char in the dict
                # then we can dec from the count
                if p_map[s[right]] == 0:
                    counter -= 1
            right += 1

            # if all chars have been found aka all values have hit zero or less
            while counter == 0:
                if s[left] in p_map:
                    p_map[s[left]] += 1
                    # when it doesnt fit the anagram we will exit the loop
                    if p_map[s[left]] > 0:
                        counter += 1
                # is the anagram we just had, the right size?
                if right-left == len(p):
                    result.append(left)

                left += 1

        return result
