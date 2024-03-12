class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            for i in range(len(mat)):
                for j in range(i+1,len(mat[0])):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for row in mat:
                row.reverse()
            return mat==target
        for _ in range(4):
            if rotate(mat):
                return True
        return False
            
        