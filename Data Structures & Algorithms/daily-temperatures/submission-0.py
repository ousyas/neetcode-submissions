class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # On initialise notre tableau de résultats avec des zéros
        result = [0] * len(temperatures)
        
        # La pile va stocker les INDEX des jours qui attendent un réchauffement
        stack = [] 
        
        for i, temp in enumerate(temperatures):
            # Tant que la pile n'est pas vide ET que la température d'aujourd'hui
            # est plus chaude que la température du jour au sommet de la pile
            while stack and temp > temperatures[stack[-1]]:
                # On récupère l'index du jour passé
                index_passe = stack.pop()
                
                # La réponse est la différence entre aujourd'hui et ce jour passé
                result[index_passe] = i - index_passe
            
            # Aujourd'hui a vérifié le passé, maintenant il se met dans la pile 
            # pour attendre son propre jour plus chaud
            stack.append(i)
            
        return result