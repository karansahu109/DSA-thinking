class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeros = []
        netPro = 1
        for i in range (len(nums)):
            if nums[i] != 0:
             product = product*nums[i]
            
            if nums[i] == 0:
                zeros.append(i)
            
        if len(zeros) > 0:
            netPro = 0


        
        for j in range (len(nums)):
            if nums[j] != 0 and netPro == 1:
              res.append(int(product/nums[j]))
            elif len(zeros) > 1 and nums[j] == 0:
              res.append(0)
            elif len(zeros) > 0 and nums[j] == 0:
              res.append(int(product))
            elif netPro == 0:
                res.append(int(netPro/nums[j]))
            


              
              
        return res
            

          
        