def recc_plus(nbre,dic):
        results = []
        k = 0
        if (nbre +1 not in dic):           
            return 1
        else:
            #dic.pop(nbre)
            return 1+recc_plus(nbre+1,dic)
def recc_moins(nbre,dic):
        results = []
        k = 0
        if (nbre -1 not in dic):
            return 1
        else:
            #dic.pop(nbre)
            return 1+recc_moins(nbre-1,dic)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        j = 0
        if nums == []:
            return 0
        for num in nums:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num] = 1
        for num in dic:           
            k = recc_moins(num,dic) + recc_plus(num,dic) -1
            print(k)
            if k > j:
                j = k
        return j

