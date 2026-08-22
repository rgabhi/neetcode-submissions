class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = ('+', '-', '/', '*')
        for tok in tokens:
            if tok in ops:
                num2 = st.pop()
                num1 = st.pop()
                if tok == '+':
                    num1 = num1 + num2
                elif tok == '-':
                    num1 = num1 - num2
                elif tok == '*':
                    num1 = num1*num2
                else:
                    if num1 != 0:
                        sign = (num1//abs(num1))*(num2//abs(num2))
                        num1 = sign*(abs(num1)//abs(num2))
                st.append(num1)
            else:
                st.append(int(tok))
            # print(st)
        return st[-1]
                
            


        