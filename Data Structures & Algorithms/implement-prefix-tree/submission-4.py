class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []          # liste d'enfants
    def ajouter(self, enfant):
        self.enfants.append(enfant)
        return enfant
    def est_feuille(self):
        return len(self.enfants) == 0
class PrefixTree:
    def __init__(self):
        self.foret = []
    def insert(self, word: str) -> None:
        foret = self.foret
        def insert_rec(i,foret):
            if i == len(word):
                foret.append(1)
                return
            for noeud in foret:
                if (noeud !=1) and (word[i] == noeud.valeur):
                    foret = noeud.enfants
                    insert_rec(i+1,foret)
                    return
            foret.append(Noeud(word[i]))
            foret = foret[-1].enfants
            insert_rec(i+1,foret)
        insert_rec(0,foret)
    def search(self, word: str) -> bool:
        foret = self.foret
        def search_rec(i,foret):
            if i == len(word):
                return 1 in foret
            for noeud in foret:
                if (noeud !=1) and (word[i] == noeud.valeur):
                    foret = noeud.enfants
                    return search_rec(i+1,foret)
            return False
        return search_rec(0,foret)
    def startsWith(self, prefix: str) -> bool:
        foret = self.foret
        def start_rec(i,foret):
            if i == len(prefix):
                return True
            for noeud in foret:
                if (noeud !=1) and(prefix[i] == noeud.valeur):
                    foret = noeud.enfants
                    return start_rec(i+1,foret)
            return False
        return start_rec(0,foret)
        