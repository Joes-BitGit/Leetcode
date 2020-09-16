# DESCRIPTION
# You are given an array of positive integers w
# where w[i] describes the weight of ith index (0-indexed).

# We need to call the function pickIndex()
# which randomly returns an integer in the range [0, w.length - 1].
# pickIndex() should return the integer proportional to its weight in the w array.
# For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%)
# while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

# More formally, the probability of picking index i is w[i] / sum(w).


# EXAMPLE 1:

# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

# EXAMPLE 2:

# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.


# Constraints:

# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.

class Solution:
    '''
    Time: O(N), must iterate through the entire array
    Space: O(N), for the array of the prefix sum
    '''

    def __init__(self, w: List[int]):
        # creates a prefix sum
        self.prefix_sum = []
        prefix_sum = 0
        for i in w:
            prefix_sum += i
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        rand_num = self.total_sum * random.random()
        left = 0
        right = len(self.prefix_sum)

        while left < right:
            mid = left + (right - left) // 2
            # want to keep the leftmost result as
            # rand_num is a float and needs to be in a range
            if rand_num > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
