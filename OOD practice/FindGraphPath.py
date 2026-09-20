'''
给一堆边的list
求所有起点到终点的对 返回list
比如任务1到任务2 任务2到任务3 简化路径成 任务1->任务3 有环的话就是任务无法完成 返回所有有效的任务完成路径（只需要起点终点）
'''

# clarify
# 一个节点是否可以走到很多节点（分叉）？ 是的
# 是否可能有环？ 是的
# 有向图还是无向图？ 有向
# is [start,end] == ["A", "A"] valid? Yes 

# input :  edges = [["A", "B"], ["A", "C"], ["C", "D"]]

# 所有出度为0为end 入度为0为start

from typing import List
from collections import defaultdict, deque

class Solution:

    def find_path(self, edges:List[List[str]]) -> List:


        res = []
        graph = defaultdict(list) # 有分叉
        in_degree = defaultdict(int)

        for node, nei in edges:
            if node == nei:  # ["A", "A"] valid 自环单独处理
                res.append([node, node])

        # construct directed graph & in_degree 
        for node, nei in edges:

            graph[node].append(nei)
            in_degree[nei] += 1
            if node not in in_degree: # all nodes should be in the in_degree dict
                in_degree[node] = 0

        # start from the start node
        for node in list(graph): # list() 快照：BFS里graph[curr]会往defaultdict塞叶子节点，直接遍历会报RuntimeError
            # if node is start node, use a queue to find all ends of it.
            if in_degree[node] == 0:
                queue = deque([node])
                visited = {node} # persist iteration from graph cycles
                ends = set() # ensuring no repeated ends; we have multiple ways for one node

                while queue:

                    curr = queue.popleft()

                    if curr not in graph or not graph[curr]:
                        ends.add(curr)
                    
                    for nei in graph[curr]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)

                for end in ends:
                    res.append([node, end])

        return res
    

