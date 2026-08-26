class Solution:
    def simplifyPath(self, path: str) -> str:
        li = path.split('/')
        st = []
        for w in li:
            if w == '' or w == '.':
                continue
            elif w == '..':
                if st:
                    st.pop()
            else:
                st.append(w)
        ans = []
        while st:
            ans.append(st.pop())
        ans.reverse()
        return "/" + "/".join(ans)
        