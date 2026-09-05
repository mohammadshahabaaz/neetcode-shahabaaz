class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = text.replace(" ", "")
        L, R = 0, len(s) - 1
        lowerSt = toLowerCase(st)
        while L < R:
            if st[R] != st[L]:
                return False
            L += 1
            R -= 1
        return True