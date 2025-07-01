class Solution:
    def scoreOfString(self, s: str) -> int:
        list_string = []
        for i in range(len(s)-1):
            sum_s = abs(ord(list(s)[i]) - ord(list(s)[i+1]))
            list_string.append(sum_s)
        return sum(list_string)
