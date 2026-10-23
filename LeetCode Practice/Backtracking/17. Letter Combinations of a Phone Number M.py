from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        # combinations - 4^n (time)因为每次4个选一个，选n; O(L) (space)
        # backtracking - enumerate all possibilities
        # 递归不能进入同index的digit；树枝本来就不会有重复的(号码代表的字母不会重复)

        n = len(digits)

        if not digits:
            return []
        
        res = []
        path = []

        char_dict = {
            2: ['a', 'b', 'c'], 
            3:['d','e','f'], 
            4:['g', 'h', 'i'], 
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'], 
            8:['t', 'u', 'v'], 
            9:['w', 'x', 'y', 'z']
            }

        def backtracking(index) -> None:

            if len(path) == n:
                res.append(''.join(path))
                return

            num = int(digits[index])
            chars = char_dict[num] # 取出这个数字里面的char列表，for循环遍历 + 递归下一个数

            for char in chars:

                path.append(char)

                backtracking(index + 1) # index不可以重复

                path.pop()

        backtracking(0)
        return res
        
            
# 递归栈深度：n
# 时间 4的n次方 （每个数字的字母列表最长是4）n次4选1