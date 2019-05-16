class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = 0
        out = []
        for i in range(len(digits)):
            val += digits[i] * 10 ** (len(digits)-i-1)
        val += 1
        for i in str(val):
            out.append(int(i))
        return out
