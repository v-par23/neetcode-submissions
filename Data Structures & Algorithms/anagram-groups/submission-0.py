from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for i in strs:
            val = tuple(sorted(i))
            hashmap[val].append(i)
        return list(hashmap.values())