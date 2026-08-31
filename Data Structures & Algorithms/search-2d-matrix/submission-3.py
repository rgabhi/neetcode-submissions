class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n= len(matrix[0])
        l = 0
        r = m*n - 1
        while l <= r:
            mid = (l + r)//2
            i = mid//n
            j = mid%n
            # print("l:", l ,"r:", r, 'mid:', mid)
            # print('i:',i, 'j:',j)
            print(matrix[i][j])
            if matrix[i][j] == target:
                # print('mil gaya')
                return True
            elif matrix[i][j] < target:
                # print('l badha')
                l = mid + 1
            else:
                # print('r ghataa')
                r = mid - 1
        return False
        