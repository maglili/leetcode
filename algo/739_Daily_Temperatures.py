class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        ans = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last_idx = stack.pop()
                ans[last_idx] = i - last_idx
            stack.append(i)
        return ans


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))
