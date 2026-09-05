class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            if s[R] != s[L]:
                return False
            L += 1
            R -= 1
        return True