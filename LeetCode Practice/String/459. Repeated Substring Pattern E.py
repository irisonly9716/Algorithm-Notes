class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # approach1: built-in KMP in python
        # t = s + s, get rid of t[0] and t[-1]. t.find(s)

        n = len(s)
        if n == 1:
            return False

        t = s + s
        t = t[1:2*n - 1]

        # t.find(s) returns the first index s appears in t, if it returns -1, s doesn't appear.
        return t.find(s) >= 0
        

        '''
        # approach2: KMP algorithm
        # KMP法 先组成前缀表
        # 如果n - prefix[-1]能够被n整除 那么s就是由重复子串组成的

        def getPrefix(s:list) -> list:

            j = 0
            n = len(s)
            prefix = [0] * n

            for i in range(1, n):
                # 求前缀表这里必是while
                while s[j] != s[i] and j > 0:
  
                    j = prefix[j - 1]

                if s[j] == s[i]:
                    j += 1

                
                prefix[i] = j

            return prefix

        n = len(s)

        prefix = getPrefix(s)

        # 要返回的是 s存在最长相等前后缀 【且】 最小重复字符串 能被n整除 的bool值
        return prefix[-1] != 0 and n % (n - prefix[-1]) == 0
        '''

