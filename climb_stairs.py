class Solution:
    def climbStairs(self, n: int) -> int: # recursive
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    def climbStairs(self, n: int) -> int: # iterative bottom up
        if n == 0 or n == 1:
            return 1
        memo = {}
        memo[0] = memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] +  memo[i - 2]
        return memo[n]
    
    def climbStairs(self, n: int) -> int: # space optimised

        if n == 0 or n == 1:
            return 1

        one, two = 1, 1

        for i in range(2, n + 1):
            temp = one
            one = one + two
            two = temp
        
        return one