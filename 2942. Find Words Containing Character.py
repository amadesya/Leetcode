class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        find_words = []
        for i in range(len(words)):
            if x in words[i]:
                find_words.append(i)
        return find_words