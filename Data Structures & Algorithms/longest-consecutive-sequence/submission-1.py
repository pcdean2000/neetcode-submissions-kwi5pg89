class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        sequences = []
        max_length = 0
        for num in nums:
            found = False
            for sequence in sequences:
                if sequence[-1] + 1 == num:
                    sequence.append(num)
                    found = True
                if len(sequence) > max_length:
                    max_length = len(sequence)
            if not found:
                sequences.append([num])
            if max_length == 0:
                max_length = 1
        
        return max_length