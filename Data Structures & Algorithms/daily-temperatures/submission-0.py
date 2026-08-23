class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        monoStack = []
        res = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while monoStack and t > monoStack[-1][0]:
                stackT, stackI = monoStack.pop()
                res[stackI] = i - stackI
            monoStack.append([t,i])
        return res

                


