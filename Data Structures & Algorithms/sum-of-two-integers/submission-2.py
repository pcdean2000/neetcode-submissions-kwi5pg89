class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            a &= mask
            b &= mask
            c = (a & b) << 1
            a ^= b
            b = c
        return ~(a ^ mask) if a > max_int else a