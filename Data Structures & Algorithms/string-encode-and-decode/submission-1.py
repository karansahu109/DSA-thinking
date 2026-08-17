class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        
        for st in strs: 
           s += str(len(st))
           s +='#'
           s += st
        return s
        # len#''

    def decode(self, s: str) -> List[str]:
        decodeList = []
        i = 0;
        while (i< len(s)):
            #2 pointer game
            j = i
            while s[j] != '#':
                j+= 1
            length = int(s[i:j])
            decodeList.append(s[j+1:j+1+length])
            i = j+1+length
            
                
        
        return decodeList
