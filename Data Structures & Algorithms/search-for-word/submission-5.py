class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def backtrack(i, j, k):
            # k = indice de la lettre du mot qu'on cherche à matcher
            if k == len(word):
                return True                      # tout le mot est trouvé
        # garde : hors grille OU lettre ne correspond pas
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

        # marquer la case comme visitée (choisir)
            temp = board[i][j]
            board[i][j] = '#'                    # '#' = case occupée, ne peut être reprise

        # explorer les 4 voisins ; si l'un réussit, on propage True
            found = (backtrack(i+1, j, k+1) or
                    backtrack(i-1, j, k+1) or
                    backtrack(i, j+1, k+1) or
                    backtrack(i, j-1, k+1))

            board[i][j] = temp                   # défaire (backtrack) : on libère la case

            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
        
            