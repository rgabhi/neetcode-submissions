class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records=[]
        for op in operations:
            if op == 'C':
               records.pop()
            elif op == 'D':
                prev = records.pop()
                new = int(prev)
                new *=2
                new = str(new)
                records.append(str(prev))
                records.append(new)
            elif op == '+':
                prev1 =  int(records.pop())
                prev2 = int(records.pop())
                new = str(prev1 + prev2)
                records.append(str(prev2))
                records.append(str(prev1))
                records.append(new)
            else:
                records.append(str(op))
            print(records)

        return sum(map(int, records))



                

        