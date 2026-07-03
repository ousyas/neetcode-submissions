def dic(t):
    d={}
    for i in t:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]=d[i]+1
    return d
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums)
        result = []
        maxi = len(nums) - len(s) +1
        r = {}
        j = 1
        d = dic(nums)
        for num in d:
            r.setdefault(d[num], []).extend([num])
        for i in range(maxi+1):
            if i in r:
                result = result+r[i]
        dictio = {}
        res = []
        for l in result:
            if l not in dictio.keys():
                dictio[l] = 1
                res.append(l)
        print(r)
        return res[len(res)-k:len(res)]


