# DESCIRPTION
# A company is planning to interview 2n people.
# Given the array costs where costs[i] = [aCosti, bCosti],
# the cost of flying the ith person to city a is aCosti,
# and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city
# such that exactly n people arrive in each city.

# EXAMPLE 1:
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

# EXAMPLE 2:
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859

# EXAMPLE 3:
# Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# Output: 3086


# Constraints:
# 2n == costs.length
# 2 <= costs.length <= 100
# costs.length is even.
# 1 <= aCosti, bCosti <= 1000


class Solution:
    '''
    Time: O(N log N), sorting the refund array
    Space: O(N), space for refund array
    '''

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Problem description: 2N so divide by 2
        # also costs length will always be even
        N = len(costs)//2
        min_cost = 0
        a_cost = 0
        refund = []
        # sum A costs
        # also create refund array
        for a, b in costs:
            # grab all the cost for location a
            # as if you were to send everyone their
            a_cost += a
            # now sub the b ticket with the a ticket
            refund.append(b-a)

        # sorted in ascending order
        refund.sort()

        # take the largest differences aka refund
        # since we dont car which one was picked just the sum
        b_cost = sum(refund[:N])

        return a_cost+b_cost
