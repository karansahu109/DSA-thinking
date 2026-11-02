class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        monoStack = []
        #this below is my thought Problem
        
        # for i in range(len(temperatures)):
        #     if not monoStack:
        #         monoStack.append((temperatures[i],i))
        #     while monoStack[-1][0] < tempeartures[i]:
        #         monoStack.pop() = temp , j
        #         res[j] = i - j
            
        for i in range(len(temperatures)):
            while monoStack and monoStack[-1][0] < temperatures[i]:
                #wrong monoStack.pop() = temp , j
                temp , j = monoStack.pop() 
                # and the res is for j (important)
                res[j] = i - j
            monoStack.append((temperatures[i],i))
        return res
            
            







        # for i in range(len(temperatures)):
        #     j = i
        #     while j < len(temperatures) :
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j - i
        #             break
        #         j += 1

        return res 
                


