class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        if k == 0 or n == 0:
            return []
        
        res = []
        path = []

        def backtracking(start):

            if len(path) == k:
                res.append(path.copy())
                return 

            # for i in range(start, n - (k - len(path)) + 2)  # Trim
            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1)
                path.pop()


        backtracking(1)
        return res

# TC:O(C(n,k))
# SC:O(k)