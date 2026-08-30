class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)

        print(x)
        print(y)

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if (x[i] != y[i]):
                return False

        return True