class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        minLength = min(len(word1), len(word2))

        for i in range(minLength):
            result.append(word1[i])
            result.append(word2[i])

        result.extend([word1[minLength:], word2[minLength:]])

        return ''.join(result)