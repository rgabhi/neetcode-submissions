class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord = {c:i for i, c in enumerate(order)}
        def comp(word):
            return [ord[c] for c in word]
        return words == sorted(words, key=comp)