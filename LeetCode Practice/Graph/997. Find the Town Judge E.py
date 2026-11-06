from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        # approach: Directed Graph / election principle??
        # if a trusts b, a is not able to be the town judge.

        graph = defaultdict(set)
        impossible = set()

        # a trusts b, b -> a
        for a, b in trust:
            graph[b].add(a)
            impossible.add(a)

        # we should not check if the person is in graph
        # edge case: only one person in the town, they don't trust anybody
        for person in range(1, n + 1):
            if person not in impossible and len(graph[person]) == n - 1:
                return person


        return -1

# TC: O(n + t), t = len(trust)
# SC: O(n + t) graph + impossible set
