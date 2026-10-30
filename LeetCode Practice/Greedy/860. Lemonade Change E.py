class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        
        # approach: greedy
        # use bigger bill first

        five = 0
        ten = 0
        twenty = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            else: # 20
                if ten < 1:
                    if five < 3:
                        return False
                    else:
                        five -= 3
                else:
                    ten -= 1
                    if five < 1:
                        return False
                    five -= 1
    
                twenty += 1

        return True

# TC:O(n)
# SC:O(1)
