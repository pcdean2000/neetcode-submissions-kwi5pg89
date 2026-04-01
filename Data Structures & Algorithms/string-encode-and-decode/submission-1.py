class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        separator = str(chr(0) + chr(1) + chr(1) + chr(0))
        return str(length) + separator + separator.join(strs)

    def decode(self, s: str) -> List[str]:
        separator = str(chr(0) + chr(1) + chr(1) + chr(0))
        length = int(s.split(separator, 1)[0])
        content = s[s.find(separator) + len(separator):]
        return content.split(separator) if length > 0 else []