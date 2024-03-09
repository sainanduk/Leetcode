class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic={j:[]for j in range(n)}
        for i in edges:
            u,v=i
            dic[u].append(v)
            dic[v].append(u)
        visted=set()
        def dfs(source):
            visted.add(source)
            for i in dic[source]:
                if i not in visted:
                    dfs(i)
        dfs(source)
        print(visted)
        return destination in visted
            
            
        