# DESCRIPTION
# Given two lists of closed intervals,
# each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes
# the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty,
# or can be represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


# EXAMPLE:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Note:
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9


class Solution:
    '''
    Time: O(N + M), N is the A and M the list of B
    Space: O(1), since output array is not considered in complexity
    '''

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        result = []
        if not A or not B or len(A) == 0 or len(B) == 0:
            return result

        a_len = len(A)
        b_len = len(B)

        a_ptr, b_ptr = 0, 0

        while a_ptr < a_len and b_ptr < b_len:
            # sets the first pair as curr
            curr_a = A[a_ptr]
            curr_b = B[b_ptr]

            # searches for the smallest gap
            # l chooses the one that is closer to the end
            l = max(curr_a[0], curr_b[0])
            # r chooses the one that is closer to the beginning
            r = min(curr_a[1], curr_b[1])

            # updates result only if the ptrs have not crossed
            if l <= r:
                result.append([l, r])

            # updates ptrs of ranges
            if curr_a[1] < curr_b[1]:
                a_ptr += 1
            elif curr_a[1] > curr_b[1]:
                b_ptr += 1
            else:
                a_ptr += 1
                b_ptr += 1

        return result
