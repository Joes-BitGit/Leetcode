# DESCRIPTION
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true
# if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# EXAMPLE 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# EXAMPLE 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# EXAMPLE 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    '''
    Time: O(R + M), where R is the len of ransom note and M is the magazine
    Space: O(R) -> O(1), since there will be at most 26 keys in dict
    '''

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        take the magazine put it in a hashtable with the letters being the key and the values being how many
        times the chars appear in the string
        Next iterate over the ransomentoe if the char is in the table dec the table 
        if the entry is 0 or not in table return false
        else dec the value by 1
        '''
        # if the ransomNote asks for more letters than we have
        # then it is impossible to build the note
        if len(ransomNote) > len(magazine):
            return False

        note = {}
        # fill table from the magazine
        for i in magazine:
            if i in note:
                note[i] += 1
            else:
                note[i] = 1
        # check the ransom note letters
        for c in ransomNote:
            if c not in note or note[c] <= 0:
                return False
            else:
                note[c] -= 1
        return True
