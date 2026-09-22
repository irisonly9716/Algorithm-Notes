from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        
        # appraoch:hashmap, {[letter:count], ...}; compare the freq of each letter word by word, min(freq1, freq2).

        # use the frequencies of letters in first word as a start.
        counter = Counter(words[0])

        for word in words[1:]:

            freq = Counter(word)

            for letter, count in counter.items():
                # everytime we need the minumum frequency of each letter accross all words
                counter[letter] = min(freq[letter], counter[letter])

        # record the answer
        ans = []
        for letter, count in counter.items():
            for _ in range(count):
                ans.append(letter)

        return ans
        
# TC:O(L) L is the length of all words 
# SC:O(26) the words have 26 different letters only.
