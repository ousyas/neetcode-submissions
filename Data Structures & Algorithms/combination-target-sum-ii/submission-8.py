class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        chemin = []
        nums = sorted(candidates)
        self.curr =-99
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i) 
        #print(dic)
        def backtrack(i):
            # cas de base : on a pris une décision pour chaque élément
            if i == len(candidates):
                return            
            chemin.append(nums[i])
            #print(chemin,self.curr,'indice:',i)
            if sum(chemin) == target:
                #if  chemin not in res:
                res.append(chemin[:])  # copie du chemin courant
                    #chemin.pop()
                #return
            if sum(chemin) > target:
                chemin.pop()
                return
            backtrack(i + 1)            
                # on DÉFAIT le choix (backtrack)
            chemin.pop()           
                # choix 2 : on NE PREND PAS nums[i]
            backtrack(max(dic[nums[i]])+1)
        backtrack(0)
        return res
        