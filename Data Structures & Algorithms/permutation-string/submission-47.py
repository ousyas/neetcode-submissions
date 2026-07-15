class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        dic_s1 = {}
        dic = {}
        l = 0
        i = 0
        for k in range(len(s1)):
            if s1[k] not in dic_s1.keys():
                dic_s1[s1[k]] = 1
            else:
                dic_s1[s1[k]] += 1
        while (dic != dic_s1) and i < len(s2):
            if s2[i] not in dic.keys():
                dic[s2[i]] = 1
            else:
                dic[s2[i]] += 1
            if i-l == len(s1):
                if dic[s2[l]]>1:
                    dic[s2[l]]-=1
                else:
                    dic.pop(s2[l])
                l+=1
            i+=1
        if dic == dic_s1:
            return True
        return False
