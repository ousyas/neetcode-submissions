class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return'-99'
        res = ""
        for s in strs:
            res+= s+ "-"
        print(res[:len(res)-1].split("-"))
        return res[:len(res)-1]
    def decode(self, s: str) -> List[str]:
        liste = s.split("-")
        if s == '-99':
            return []
        return liste