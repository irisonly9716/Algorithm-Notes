class Solution:
    def isHappy(self, n: int) -> bool:
        
        # approach: use a set to record every computing result in the progress.
        # if it's a happy num, the result in progress will never repeat.
        # compute till the result == 1 or the result gets repeated.

        res_set = set()

        # when n == 1, jump out of this while loop, return True
        while n != 1:

            string = str(n)
            result = 0

            # compute new result
            for char in string:
                num = int(char)
                result += num ** 2
                
            if result in res_set:
                return False

            res_set.add(result)
            n = result # set result as n

        return True

# TC: O(the number of results * average length of the results) -> o(log n)
# SC: O(the number of results + length of the biggest n) —> O(log n)  
# why + in SC? the string will be discarded everytime we run the loop
