# Not optimized need to create a better solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub = []
        ptr = 0
        max_len = 0

        if s == "":
            return 0
        else:
            for x in range(0, len(s)):

                if s[x] not in sub:
                    sub.append(s[x])


                else:
                    sub = []
                    sub.append(s[x])

                if len(sub) >= max_len:

                    max_len = len(sub)

        return max_len
