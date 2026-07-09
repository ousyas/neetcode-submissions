class TimeMap:

    def __init__(self):
        self.dic={}     

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((value,timestamp))
        else:
            self.dic[key] = [(value,timestamp)]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        l = self.dic[key]
        i = -1
        while -i<=len(l):
            val_prev,time_prev = l[i]
            if timestamp >= time_prev:
                return val_prev
            else:
                i-=1
                print(l)
        print(i)
        return ""
        
        
