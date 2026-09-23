class Solution:
    def reverseWords(self, s: str) -> str:

        # approach: split the words and reverse them
        return " ".join(reversed(s.split()))

        '''
        # 为每个word跳过whitespace 然后反转
        # O(n) O(n)

        i = 0
        words = []
        n = len(s)

        while i < n:

            while i < n and s[i] == " ":
                i += 1

            if i >= n: # 无法省略此处！！！
                break

            start = i
            while i < n and s[i] != ' ':
                i += 1

            words.append(s[start:i])
            
        return ' '.join(reversed(words))
        '''