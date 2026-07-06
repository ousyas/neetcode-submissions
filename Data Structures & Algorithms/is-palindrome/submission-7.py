class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum():
                s= s.replace(i, "")
        for j in range(-1,(-len(s)-1),-1):
            print(s[j],s[-j-1])
            if s[j].lower() != s[-j-1].lower():
                return False
        return True
        