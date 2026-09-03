class Solution:

    def encode(self, strs: List[str]) -> str:
        l = []
        for s in strs:
            l.append(str(len(s)))
            l.append("#")
            l.append(s)
        return "".join(l)

    
    def decode(self, s: str) -> List[str]:
        strs = []
        c = 0
        w = []
        while c < len(s):
            if s[c].isdigit():
                cur = s[c]
                j = 1
                while s[c+j].isdigit():
                    cur += s[c+j]
                    j+=1
                c+=j+1
                for i in range(c, int(cur)+c):
                    w.append(s[i])
                else:
                    strs.append("".join(w))
                    w.clear()
                    c += int(cur)
            else:
                c += 1
        return strs
