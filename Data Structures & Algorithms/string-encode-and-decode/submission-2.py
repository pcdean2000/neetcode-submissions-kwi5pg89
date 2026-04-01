class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = "#"
        return "".join((str(len(s)) + separator + s for s in strs))

    def decode(self, s: str) -> List[str]:
        separator = "#"
        strs = []
        while len(s) > 0:
            length = int(s[:s.find(separator)])
            elem = s[:s.find(separator) + len(separator) + length]
            strs.append(elem[s.find(separator) + len(separator):])
            s = s[s.find(separator) + len(separator) + length:]
        return strs