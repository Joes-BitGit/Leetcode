# DESCRIPTION
# There are a total of numCourses courses you have to take,
# labeled from 0 to numCourses-1.

# Some courses may have prerequisites,
# for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses?


# EXAMPLE 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.

# EXAMPLE 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.


# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

class Solution:
    '''
    Time: O(V + E), must search every node and every nodes edge
    Space: O(V + E), space required for adjacency list
    '''

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        adj_list = [[] for _ in range(numCourses)]

        # create visited array
        visited = [0 for _ in range(numCourses)]

        # create a graph
        for pair in prerequisites:
            x, y = pair
            adj_list[x].append(y)

        # search every node in the graph
        for i in range(numCourses):
            if not self.dfs(adj_list, visited, i):
                return False

        return True

    def dfs(self, adj_list, visited, i):
        # if the vertex is currently on the call stack
        # then we have found a cycle, because we have seen it before
        if visited[i] == -1:
            return False

        # this means we have reached then end of the current vertex
        # we do not need to continue searching
        if visited[i] == 1:
            return True

        # mark as currently being visited aka on the call stack
        visited[i] = -1

        # search all the neighboring vertices
        for j in adj_list[i]:
            if not self.dfs(adj_list, visited, j):
                return False

        # finished visiting this vertex
        visited[i] = 1
        return True
