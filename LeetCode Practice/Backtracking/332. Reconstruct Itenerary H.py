from collections import defaultdict
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # approach: directed graph + backtracking
        # record the final destination(no adjecent nodes anymore) first and then start
        # Eulerian path: a path that visits every edge exactly once.
        # The problem is guaranteed to have at least one valid itinerary. So we can use DFS to find the Eulerian path.

        graph = defaultdict(list) # {start:[destinations]}
        res = [] # reversly record destinations
        for start, des in tickets:
            graph[start].append(des)

        for city in graph.values():
            city.sort(reverse=True) # go to the smallest city first.

        def dfs(city) -> None:

            # ⭐ while loop is important, because we need to keep going to the next destination until there is no more destination.
            while city in graph and graph[city]:

                destination = graph[city].pop()
                dfs(destination)

            # record the final destination first, then backtrack to the previous city.
            res.append(city)
        
        dfs('JFK')

        return res[::-1]


# O(E log E) + O(V + E)
# O(V + E)