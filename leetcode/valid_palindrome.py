class Solution:
    def isPalindrome(self, s: str) -> bool:
        _stack = []
        lst = list(s)
        if not s:
            return True

        for ele in s:
            if ele.isalpha() or ele.isdigit():
                _stack.append(ele)
        print(lst)
        for x in range(0, len(lst)):
            if lst[x].isalpha() or lst[x].isdigit():
                if lst[x].casefold() != _stack.pop().casefold():
                    return False

        return True
