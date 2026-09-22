from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # approach: hashmap

        counter = Counter(magazine)

        for char in ransomNote:
            if counter[char] <= 0:
                return False

            counter[char] -= 1

        return True

# TC:O(n + m)
# SC:O(n)

