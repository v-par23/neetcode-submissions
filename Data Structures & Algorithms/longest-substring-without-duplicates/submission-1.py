class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        l = 0
        maxL = 0

        for r, let in enumerate(s):

            while let in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            maxL = max(maxL, r - l + 1)

        return maxL
            
        