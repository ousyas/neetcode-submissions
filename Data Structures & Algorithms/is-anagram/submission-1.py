def dic(t):
    d={}
    for i in t:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]=d[i]+1
    return d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return dic(t) == dic(s)
        
