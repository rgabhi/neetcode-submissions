class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for c in s:
            if c in ('(', '{', '['):
                q.append(c)
            else:
                if q and (
                        (q[-1] == '[' and c == ']') or
                        (q[-1] == '(' and c == ')') or
                        (q[-1] == '{' and c == '}')
                    ):
                    q.pop()
                else:
                    return False
        return len(q) == 0

                     

        