class Solution:
    def isValid(self, s: str) -> bool:
        pStack = []
        for i in range( len(s)):
            if ord(s[i]) == 91 or ord(s[i]) == 123 or ord(s[i]) == 40 :
                pStack.append(s[i])
            elif (len(pStack) != 0) and ( ord(s[i]) - ord(pStack[-1]) == 1 or   ord(s[i]) - ord(pStack[-1]) == 2):
                pStack.pop()
            else:
                return False
            

            
        if len(pStack) != 0:
            return False
        else:
            return True

        
        