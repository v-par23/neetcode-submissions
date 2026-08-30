class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if (x[i] != y[i]):
                return False

        # if (x == y):
        #     return True
        # else: return False



        return True