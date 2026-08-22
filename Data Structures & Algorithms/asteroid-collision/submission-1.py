class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            alive = True
            while st and st[-1] > 0 and ast < 0:
                if st[-1] < -ast:
                    st.pop()
                elif st[-1] == -ast:
                    st.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                st.append(ast)
        return st 
            
        