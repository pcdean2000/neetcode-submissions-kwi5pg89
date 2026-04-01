class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            c = (a & b) << 1
            a = (a ^ b) & mask
            b = c & mask
        return ~(a ^ mask) if a > max_int else a