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
        result = []
        d=dic(nums)
        d_sorted=list(d.values())
        d_sorted.sort(reverse = True)
        print(d_sorted)
        for i in range(k):
            for cle, valeur in d.items():
                if valeur == d_sorted[i]:
                    if cle not in result:
                        result.append(cle)
        return result
