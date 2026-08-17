class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numTable = {}
        if len(s) != len(t):
            return False
        for char in s:
            numTable[char] = numTable.get(char,0) + 1
        
        for char in t:
            if char not in numTable:
                return False
            numTable[char] -= 1

            if numTable[char] <0:
                return False
            
        
        return True

        