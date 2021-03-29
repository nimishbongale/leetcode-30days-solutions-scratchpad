class Solution:
    def findComplement(self, num: int) -> int:
        return int('0b'+''.join(['1' if i=='0' else '0' for i in bin(num)[2:]]),2)
