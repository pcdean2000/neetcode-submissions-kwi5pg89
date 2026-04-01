# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def qsort(pairs, s, e):
            if e - s + 1 <= 1:
                return pairs

            pivot = pairs[e]
            left = s
            
            for i in range(left, e):
                if pairs[i].key < pivot.key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1
            
            pairs[e] = pairs[left]
            pairs[left] = pivot

            pairs = qsort(pairs, s, left - 1)
            pairs = qsort(pairs, left + 1, e)

            return pairs
        
        return qsort(pairs, 0, len(pairs) - 1)
