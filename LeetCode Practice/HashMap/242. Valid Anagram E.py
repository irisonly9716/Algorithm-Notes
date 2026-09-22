from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # approach:hashmap, iterate string s, store {[english letter:count], ...}. Then iterate string t.

        # this edge case must be included, otherwise we need to check if all counts of letters are 0 in the end.
        if len(s) != len(t):
            return False

        # we can use letter_dict = Counter(s)
        letter_dict = Counter()

        for letter in s:
            
            letter_dict[letter] += 1


        for letter in t:

            if letter_dict[letter] <= 0:
                return False
            else:
                letter_dict[letter] -= 1

        return True

# TC:O(n+m)
# SC:O(n) -> in the worst case, all letters appear once.

