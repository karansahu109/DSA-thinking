class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n - 1
        while l<=r:
            mid = l + (r-l)//2
            row = mid//n
            col = mid%n
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False



        # rowLen = len(matrix[0])
        # colLen = len(matrix)
        
        # for col in range(colLen):
        #     l, r = 0 , rowLen - 1
        #     if target >= matrix[col][l] and target <= matrix[col][r]:
        #         while l<=r:
        #             mid = l +(r-l)//2
        #             if target > matrix[col][mid]:
        #                 l = mid+1
        #             elif target < matrix[col][mid]:
        #                 r = mid-1
        #             else:
        #                 return True
        #     else:
        #         continue
        # return False

        