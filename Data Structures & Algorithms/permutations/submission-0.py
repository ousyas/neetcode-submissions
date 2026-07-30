class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chemin = []
        self.k = 0
        def backtrack(reste):
            if not reste:
                res.append(chemin[:])
                return
            for x in reste:
                chemin.append(x)
                nouveau_reste = [y for y in reste if y != x]
                backtrack(nouveau_reste)     # ← nouvel appel = NOUVELLE boucle
                chemin.pop()
        backtrack(nums)
        return res
