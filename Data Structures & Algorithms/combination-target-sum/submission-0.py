class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        chemin = []
        def backtrack(i):
            # cas de base : on a pris une décision pour chaque élément
            if i == len(nums):
                if sum(chemin) == target:
                    res.append(chemin[:])   # copie du chemin courant
                return
            
            # choix 1 : on PREND nums[i]
            chemin.append(nums[i])
            #print(chemin,i)
            if sum(chemin) == target:
                res.append(chemin[:])   # copie du chemin courant
                #return
            elif sum(chemin) > target:
                chemin.pop()
                return
            backtrack(i)           
            # on DÉFAIT le choix (backtrack)
            chemin.pop()            
            # choix 2 : on NE PREND PAS nums[i]
            backtrack(i + 1)       
        backtrack(0)
        return res