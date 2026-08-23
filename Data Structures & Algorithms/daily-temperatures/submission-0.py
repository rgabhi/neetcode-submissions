class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        ans = [0]*n
        for i, temp in enumerate(temperatures):
            if not st:
                st.append(i)
            else:
                while st and temperatures[st[-1]] < temp:
                    j = st.pop()
                    ans[j] = i - j
                st.append(i)
            # print(st)
        return ans
                

        