class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''

        stack = []
        hashmap = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if stack and (char in hashmap and stack[-1] == hashmap[char]):
                stack.pop()
            else:
                stack.append(char)
        
        return not stack

