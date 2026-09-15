class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = {}          # liste d'enfants
    def ajouter(self, enfant):
        self.enfants.append(enfant)
        return enfant
    def est_feuille(self):
        return len(self.enfants) == 0
class PrefixTree:
    def __init__(self):
        self.foret = {}
    def insert(self, word: str) -> None:
        foret = self.foret
        def insert_rec(i,foret):
            if i == len(word):
                foret[1] = 1
                return
            if word[i] in foret:
                foret = foret[word[i]].enfants
                insert_rec(i+1,foret)
                return
            foret[word[i]] = Noeud(word[i])
            foret = foret[word[i]].enfants
            insert_rec(i+1,foret)
        insert_rec(0,foret)
    def search(self, word: str) -> bool:
        foret = self.foret
        def search_rec(i,foret):
            if i == len(word):
                return 1 in foret
            if word[i] in foret:
                foret = foret[word[i]].enfants
                return search_rec(i+1,foret)
            return False
        return search_rec(0,foret)
    def startsWith(self, prefix: str) -> bool:
        foret = self.foret
        def start_rec(i,foret):
            if i == len(prefix):
                return True
            if prefix[i] in foret:
                foret = foret[prefix[i]].enfants
                return start_rec(i+1,foret)
            return False
        return start_rec(0,foret)
        