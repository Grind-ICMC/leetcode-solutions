class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N

        for i in range(N - 2, -1, -1):
            u = i + 1
            while u < N and temperatures[i] >= temperatures[u]:
                if res[u] == 0:
                    u = N
                    break

                u = u + res[u]

            if u < N:
                res[i] = u - i

        return res


        





