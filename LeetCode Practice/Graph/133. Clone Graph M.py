# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Approach: Undirected Graph
        # BFS/DFS + hashmap

        if not node:
            return None

        # is this node cloned?, node:clone
        clone_dict = {}
        
        def dfs(node) -> Node|None:

            if node in clone_dict:
                return clone_dict[node] # return the cloned one

            cloned = Node(node.val)
            clone_dict[node] = cloned # ⭐ remember to add the cloned node to the dict

            for neighbor in node.neighbors:
                cloned.neighbors.append(dfs(neighbor))
            
            return cloned

        return dfs(node)

# TC: O(V + E) each node and each edge is visited once
# SC: O(V) clone_dict + recursion stack
