class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for char in s:
            if char.isalnum():
                st += char.lower()
        
        L, R = 0, len(st) - 1
        while L < R:
            if st[R] != st[L]:
                return False
            L += 1
            R -= 1
        return True