class Solution:
    def gcd(self, A, B):
        if B == 0:
            return A 
        else:
            return self.gcd(B, A % B)