class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        
        # approach: graph/ hash table
        # order = "ld", then "world" should be smaller than "word"
        # compare words one by one

        graph = {} # {["w":"followingchar"], ["o":"followingchar"], ....}
        n = len(order)

        for i in range(n):

            graph[order[i]] = order[i + 1:n]

        for i in range(1, len(words)):

            l1 = len(words[i-1])
            l2 = len(words[i])

            m = min(l1, l2)

            # 1. compare char one by one
            same_count = 0
            for j in range(m):
                if words[i-1][j] == words[i][j]:
                    same_count += 1
                    continue
                if words[i-1][j] != words[i][j]:
                    if words[i][j] not in graph[words[i-1][j]]:
                        return False
                    else:
                        break # ⭐we only care about the first difference.

            # 2. if they are same in shorter length, the shorter one should be smaller
            if same_count == m and l1 > l2:
                return False

        return True
            
# Time:  O(L), L = total characters in words
# Space: O(1), graph size is bounded by the 26-letter alphabet
