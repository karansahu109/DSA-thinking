class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers) - 1
        #we have to use the fact that array is sorted
        while l < len(numbers) - 1 and r > 0 and l<r :
            #if target > increase i 
            #if target < decrease j
            sum = numbers[l] + numbers[r]
            if target > sum:
                l += 1
            elif target < sum:
                r -= 1
            else:
                return [l+1, r+1]





        