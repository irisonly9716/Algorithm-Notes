class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        
        # approach:greedy
        # order by height DESC first and insert the position in queue

        people.sort(key=lambda x:(-x[0],x[1])) # order by height DESC
        queue = [] # empty queue to be inserted

        # [height, position key]
        for i in range(len(people)):

            queue.insert(people[i][1], [people[i][0], people[i][1]])

        return queue
            

# TC:O(n**2) sorting is O(n log n), but every queue.insert() shifts up to n elements
# SC:O(n) the new queue, which is the output