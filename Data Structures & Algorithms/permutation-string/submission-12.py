class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        dic_s1 = {}
        for k in range(len(s1)):
            if s1[k] not in dic_s1.keys():
                dic_s1[s1[k]] = 1
            else:
                dic_s1[s1[k]] += 1
        #print(dic_s1)
        i,j = 0,len(s1)
        #print(i,j)
        while j <= len(s2):
            dic = {}
            if s2[i] not in dic_s1.keys():
                i+=1
                j+=1
            else:
                for k in range(i,j):
                    if s2[k] not in dic.keys():
                        dic[s2[k]] = 1
                    else:
                        dic[s2[k]] += 1
                #print(dic)
                if dic == dic_s1:
                    return True
                else:
                    i+=1
                    j+=1
        return False
