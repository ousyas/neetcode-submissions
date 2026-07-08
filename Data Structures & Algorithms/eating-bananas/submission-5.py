class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        minimum = 1
        #rates = range(1,maximum+1)
        rate = (maximum + minimum)//2
        resultat = rate
        while minimum <= maximum:
            temp = []
            for pile in piles:
                temp.append(-(-pile//rate))
            print(sum(temp))
            if sum(temp) <= h:
                resultat = rate
                maximum = rate -1
                rate = (maximum + minimum)//2
            else:
                minimum = rate +1
                rate = (maximum + minimum)//2
        print(rate)
        return resultat
            



