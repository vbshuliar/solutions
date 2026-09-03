class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            # Find where the delimiter '#' is located
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            # The actual word sits directly after '#'
            start = j + 1
            end = start + length
            
            strs.append(s[start:end])
            
            # Move pointer directly past the extracted word
            i = end

        return strs