# DESCRIPTION
# Given a set of N people (numbered 1, 2, ..., N),
# we would like to split everyone into two groups of any size.
# Each person may dislike some other people,
# and they should not go into the same group.
# Formally, if dislikes[i] = [a, b],
# it means it is not allowed to put the people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone
# into two groups in this way.

# EXAMPLE 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# EXAMPLE 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# EXAMPLE 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false


# Constraints:

# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j]

class Solution:
    '''
    Time: O(D + N), where D is the length of disliked array and N is the input
    Space: O(D + N)
    '''

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        NO_COLOR, BLUE, RED = 0, 1, -1

        # dfs
        def blacklisted(person, color):
            # assign the person the new color
            colors[person] = color

            # person2 is each person disliked by current person
            for person2 in blacklist[person]:
                # if the disliked person has the same color
                # this means that person2 conflicts with curr person
                if colors[person2] == color:
                    return False
                # if the disliked person color has not been seen
                # then assign the disliked person the oppo color to search for
                if colors[person2] == NO_COLOR and (not blacklisted(person2, -color)):
                    return False

            return True

        # quick answers for simple cases
        if N == 1 or not dislikes:
            return True

        # dictionary that holds each disliked person
        blacklist = collections.defaultdict(list)

        # holds the color values of each person
        colors = [NO_COLOR for _ in range(N+1)]

        # fills the dictionary up with disliked persons
        for p1, p2 in dislikes:
            blacklist[p1].append(p2)
            blacklist[p2].append(p1)

        for person in range(1, N+1):
            # if the current person has not been seen and not been disliked
            if colors[person] == NO_COLOR and (not blacklisted(person, BLUE)):
                return False
        return True
