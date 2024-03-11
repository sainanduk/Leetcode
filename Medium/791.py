class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s=list(s)
        ans=[]
        for i in order:
            while i in s:
                ans.append(i)
                s.remove(i)
        ans=ans+s
        return "".join(ans)
            
        
        