class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        chemin = []
        
        def backtrack(i):
            # cas de base : on a pris une décision pour chaque élément
            if i == len(nums):
                res.append(chemin[:])   # copie du chemin courant
                return
            
            # choix 1 : on PREND nums[i]
            chemin.append(nums[i])
            backtrack(i + 1)
            
            # on DÉFAIT le choix (backtrack)
            chemin.pop()
            
            # choix 2 : on NE PREND PAS nums[i]
            backtrack(i + 1)
        
        backtrack(0)
        return res