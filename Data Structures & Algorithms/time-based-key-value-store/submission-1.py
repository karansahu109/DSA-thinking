class TimeMap:

    def __init__(self):
        self.temporalDict = {} 

    def set(self, key, value, timestamp):
        if key not in self.temporalDict:
            self.temporalDict[key] = []

        self.temporalDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.temporalDict:
            return ""
        l,r = 0 , len(self.temporalDict[key]) - 1
        ans = ""
        while l <= r:

            m = l + (r-l)//2

            if self.temporalDict[key][m][0] <= timestamp:
                ans = self.temporalDict[key][m][1]
                l = m + 1

            else:
                r = m - 1
        return ans
            

        
