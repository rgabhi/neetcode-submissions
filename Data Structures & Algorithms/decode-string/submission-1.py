class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        i = 0
        n = len(s)
        while i < n:
            print(st)
            if 'a' <= s[i] <= 'z':
                j = i + 1
                while j < n and 'a' <= s[j] <= 'z':
                    j += 1
                st.append(s[i:j])
                i = j
            elif '0' <= s[i] <= '9':
                j = i + 1
                while j < n and '0' <= s[j] <= '9':
                    j += 1
                st.append(s[i:j])
                i = j
            elif s[i] == '[':
                st.append(s[i])
                i += 1
            else:
                pattern = "" 
                while st[-1] != '[':
                    pattern = st.pop() + pattern
                st.pop()
                repeat = int(st.pop())
                pattern = pattern*repeat
                st.append(pattern)
                i += 1
        print(st)
        ans = []
        print("--------------")
        while st:
            print(ans)
            ans.append(st.pop())
        ans.reverse()
        print(ans)
        return "".join(ans)
                      
        