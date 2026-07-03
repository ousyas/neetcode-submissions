class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():  # si c'est une ouvrante
                stack.append(char)
            elif char in mapping:  # si c'est une fermante
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # caractère invalide
        return not stack
