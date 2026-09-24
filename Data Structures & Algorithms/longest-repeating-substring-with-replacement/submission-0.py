class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        counter = defaultdict(int)
        l = 0
        maxL = 0
        maxF = 0

        for r, let in enumerate(s):
            counter[let] += 1
            maxF = max(maxF, counter[let])

            while (r - l + 1) - maxF - k > 0:
                counter[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, r - l + 1) 
        
        return maxL 


