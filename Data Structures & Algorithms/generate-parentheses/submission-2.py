class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n_l = 0
        self.n_r = 0
        res = []
        self.chemin = []
        par = ['(']*n+[')']*n
        def backtrack():
            if (self.n_l>=n) and (self.n_r>=n):
                res.append("".join(self.chemin))
                return
            elif (self.n_l == self.n_r) and (self.n_l <n):       
                self.chemin.append('(')
                self.n_l+=1
                #print(self.chemin,'obligation de (')
                backtrack()
                self.chemin.pop()
                self.n_l-=1
            elif (self.n_l == n):
                #while self.n_r<n:
                self.chemin.append(')')
                self.n_r+=1
                #print(self.chemin,'obligation de )')
                backtrack()
                self.chemin.pop()
                self.n_r-=1
                #print(self.chemin,"revenir en arriere apres obligation de )")
                return
            else:
                self.chemin.append('(')
                self.n_l+=1
                #print(self.chemin,self.n_l,"choix de (")
                backtrack()
                curr = self.chemin.pop()
                if curr =='(':
                    self.n_l-=1
                    self.chemin.append(')')
                    self.n_r+=1
                elif curr ==')':
                    self.n_r-=1
                    self.chemin.append('(') 
                    self.n_l+=1   
                #print(self.chemin,self.n_l,"revenir en arriere")
                backtrack()
                curr = self.chemin.pop()
                if curr =='(':
                    self.n_l-=1
                elif curr ==')':
                    self.n_r-=1 
                return
        backtrack()    
        return res