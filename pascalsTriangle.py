def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            if i == 1:
                ans.append([1])
            elif i == 2:
                ans.append([1, 1])
            else:
                prev = ans[-1]
                nxt = [1]
                for j in range(len(prev) - 1):
                    nxt.append(prev[j] + prev[j + 1])
                nxt.append(1)
                ans.append(nxt)
        return ans
