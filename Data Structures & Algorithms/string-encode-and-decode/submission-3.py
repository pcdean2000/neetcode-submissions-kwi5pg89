class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = "#"
        return "".join((str(len(s)) + separator + s for s in strs))

    def decode(self, s: str) -> List[str]:
        separator = "#"
        strs = []
        ptr = 0
        while len(s) > ptr:
            separator_index = s.find(separator, ptr)
            length = int(s[ptr:separator_index])
            new_ptr = separator_index + len(separator) + length
            elem = s[ptr:new_ptr]
            strs.append(elem[separator_index - ptr + len(separator):])
            ptr = new_ptr
        return strs