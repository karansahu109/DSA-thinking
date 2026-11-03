class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        l , r = 0 , rowLen*colLen - 1

        while l<=r:
            mid = l + (r-l)//2
            row = mid//colLen
            col = mid%colLen
            if (matrix[row][col]<target):
                l = mid+1
            elif (matrix[row][col]>target):
                r = mid-1
            else:
                return True
        return False
            



        # for row in range(rowLen):
        #     l, r = 0 , colLen - 1
        #     if target >= matrix[row][l] and target <= matrix[row][r]:
        #         while l<=r:
        #             mid = l +(r-l)//2
        #             if target > matrix[row][mid]:
        #                 l = mid+1
        #             elif target < matrix[row][mid]:
        #                 r = mid-1
        #             else:
        #                 return True
        #     else:
        #         continue
        # return False

        