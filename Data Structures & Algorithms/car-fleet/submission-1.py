class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        track = [0]*target
        for p,s in zip(position, speed):
            track[p] = s
        fleet = 0
        maxTime = 0
        for i in range(target-1,-1,-1):
            if track[i] != 0:
                time = (target - i)/track[i]
                if time> maxTime:
                    fleet += 1
                    maxTime = time
        return fleet




    #  pair = [[p,s] for p,s in zip(position, speed)]
    #  stack = []
    #  for p,s in sorted(pair)[::-1]:
    #      stack.append((target - p) / s)
    #      if len(stack) >= 2 and stack[-1] <= stack[-2]:
    #          stack.pop()
    #  return len(stack)
