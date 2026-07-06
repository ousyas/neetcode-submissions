from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # On crée des dictionnaires de "sets" pour stocker ce qu'on a déjà vu
        # defaultdict(set) permet de créer un set vide automatiquement si la clé n'existe pas
        lignes = defaultdict(set)
        colonnes = defaultdict(set)
        blocs = defaultdict(set)

        # On parcourt chaque case de la grille 9x9 une seule fois
        for i in range(9):
            for j in range(9):
                valeur = board[i][j]
                
                # Si la case est vide, on passe à la suivante
                if valeur == '.':
                    continue
                
                # On identifie dans quel bloc 3x3 on se trouve (ex: bloc (0,1) ou (2,2))
                id_bloc = (i // 3, j // 3)

                # Si la valeur est DÉJÀ dans la ligne i, la colonne j ou le bloc correspondant
                # Alors le Sudoku est invalide !
                if (valeur in lignes[i]) or (valeur in colonnes[j]) or (valeur in blocs[id_bloc]):
                    return False
                
                # Sinon, on ajoute cette valeur dans nos sets pour s'en souvenir
                lignes[i].add(valeur)
                colonnes[j].add(valeur)
                blocs[id_bloc].add(valeur)
                
        # Si on a fini tout le tableau sans erreur, alors c'est valide
        return True