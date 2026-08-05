class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.chemin = []
        res = []
        self.curr=''
        self.decision = True
        def backtrack(i):
            #print(i,len(s))
            #print(self.chemin,i)
            if i==len(s):
                if self.decision:
                    res.append(self.chemin[:])
                    #print(res)                
                return
            self.curr+=s[i]
            maint = self.curr[:]
            if self.curr == self.curr[::-1]:
                self.chemin.append(self.curr)
                self.curr = ''
                self.decision = True
                backtrack(i+1)
                self.chemin.pop()
                self.curr = maint
                self.decision = False
                backtrack(i+1)
            else:
                self.decision = False
                backtrack(i+1)
            #print(self.chemin)
        backtrack(0)
        return res
            
            