class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numTable = {}
        if len(s) != len(t):
            return False
        for i in range (len(s)):
            if s[i] not in numTable:
                numTable[s[i]] = 1
            else:
                numTable[s[i]] += 1
        for i in range (len(t)):
            if t[i] not in numTable:
                return False
            else:
                numTable[t[i]] -= 1
            
            if numTable[t[i]] < 0:
                return False
            
        
        return True

        