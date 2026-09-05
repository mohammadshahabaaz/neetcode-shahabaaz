class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "")
        L, R = 0, len(st) - 1
        st = st.lower
        while L < R:
            if st[R] != st[L]:
                return False
            L += 1
            R -= 1
        return True