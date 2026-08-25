class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        car = []
        for i in range(n):
            car.append((position[i], speed[i]))
        car.sort(key=lambda x: x[0])
        car.reverse()
        st =[]
        for c in car:
            time = (target - c[0])/c[1]
            if not st:
                st.append(time)
            else:
                if time <= st[-1]:
                    continue
                else:
                    st.append(time)
        return len(st)
        