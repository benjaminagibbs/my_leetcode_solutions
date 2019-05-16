class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        js = []
        out = 0
        for i in J:
            js.append(i)
        for i in S:
            if i in js:
                out = out + 1
        return out
