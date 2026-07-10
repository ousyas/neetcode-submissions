class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        result = 1
        r = 0
        if len(s)==0:
            return 0
        i = 0
        while i< len(s):
            if s[i] not in dic.keys():
                dic[s[i]] = i
                r+=1
                i+=1
            else:
                if result < len(dic):
                    result = len(dic)
                i = dic[s[i]]+1
                dic = {s[i]:i}
                #if s[i] ==s[i-1]:
                 #   r = 1
                #else:
                r = 1
                i+=1
        return max(result,r)


