# DESCRIPTION

# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h, k),
# where h is the height of the person and
# k is the number of people in front of this person
# who have a height greater than or equal to h.
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.


# EXAMPLE 1

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

class Solution:
    '''
    Time: O(N LOG N), for the sort 
    Space: O(1)
    '''

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=self.by_h_k)
        result = []
        for p in people:
            # inserting p at index k in result queue
            result.insert(p[1], p)
        return result

    def by_h_k(self, people):
        # sorts by largest height descending
        # if they are equal
        # then by the k value ascending
        return -people[0], people[1]
