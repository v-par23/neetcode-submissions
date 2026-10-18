class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ts = sorted(t)
        ss = sorted(s)

        if ts == ss:
            return True
        return False