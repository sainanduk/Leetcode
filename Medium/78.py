class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(1,len(nums)+1):
            comb=list(combinations(nums,i))
            for j in comb:
                res.append(list(j))
        res.append([])
        return res
            