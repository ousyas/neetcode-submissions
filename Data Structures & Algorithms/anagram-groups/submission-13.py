class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        l = []
        for str in strs:
            for c in str:
                l.append(c)
            l.sort()
            t = tuple(l)
            if t not in d:
                d[t] = [str]
                print(d[t])
            else:
                d[t].extend([str])
            l = []
        return list(d.values())


