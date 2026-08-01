class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n= len(people)
        people.sort()
        i = 0
        j = n - 1
        cnt = 0
        curr = 0
        while i <= j:
            curr = people[i] + people[j]
            if i == j:
                cnt += 1
                break
            if curr <= limit:
                cnt += 1
                i += 1
                j -= 1
            else:
                cnt += 1
                j -= 1
        return cnt
        