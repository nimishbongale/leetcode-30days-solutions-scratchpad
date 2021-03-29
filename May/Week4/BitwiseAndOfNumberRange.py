class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return m & (-1 << (0 if m == n else len(bin(m ^ n))-2))
