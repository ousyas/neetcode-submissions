def recc_plus(nbre,dic):
        if (nbre +1 not in dic):
            dic.pop(nbre)          
            return 1
        else:
            dic.pop(nbre)
            return 1+recc_plus(nbre+1,dic)
def recc_moins(nbre,dic):
        if (nbre -1 not in dic):
            dic.pop(nbre)
            return 1
        else:
            dic.pop(nbre)
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
        l = list(dic.keys())
        while num != 'Vide':
            k = recc_plus(num,dic)
            dic[num] = 1
            k+= recc_moins(num,dic) -1
            if k > j:
                j = k
            l = list(dic.keys())
            num = next(iter(l), "Vide")
            print(num)
        return j
        #for num in dic:           
            #k = recc_moins(num,dic) + recc_plus(num,dic) -1
            #print(dic)
            #if k > j:
                #j = k
        #return j

