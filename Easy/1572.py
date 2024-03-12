class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        i=0
        j=0
        while j<len(mat):
            summ+=mat[i][j]
            i+=1
            j+=1
        i=len(mat)-1
        j=0
        while i>=0:
            summ+=mat[i][j]
            j+=1
            i-=1
        if len(mat)%2!=0:
            mid=len(mat)//2
            summ-=mat[mid][mid]
            return summ
        return summ
        