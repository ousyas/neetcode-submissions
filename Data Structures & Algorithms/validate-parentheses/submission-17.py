class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in par.values():
                stack.append(char)
            elif char in par:
                if stack==[] or stack[-1]!= par[char]:
                    return False
                stack.pop()
        if stack !=[]:
            return False
        return True

        
