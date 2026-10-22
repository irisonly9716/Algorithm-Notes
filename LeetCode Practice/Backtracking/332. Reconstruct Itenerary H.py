from collections import defaultdict
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # approach: directed graph + backtracking
        # record the final destination(no adjecent nodes anymore) first and then start

        graph = defaultdict(list) # {start:[destinations]}
        res = [] # reversly record destinations
        for start, des in tickets:
            graph[start].append(des)

        for city in graph.values():
            city.sort(reverse=True) # go to the smallest city first.

        def dfs(city) -> None:

            while city in graph and graph[city]:

                destination = graph[city].pop()
                dfs(destination)

            if not graph[city]:
                res.append(city)
        
        dfs('JFK')

        return res[::-1]


# O(E log E) + O(V + E)
# O(V + E)