class Solution:
    def dailyTemperatures2(self, temperatures: list):
        """
        Time Limit Exceeded
        """
        stack = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            count = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] >= temperatures[j]:
                    count += 1
                    continue
                else:
                    stack[i] = count
                    count = 1
                    break
        return stack

    def dailyTemperatures(self, temperatures: list):
        stack = []
        for i in range(len(temperatures)):
            stack.append(temperatures[i])
            pass

        return stack


if __name__ == "__main__":
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
    print(Solution().dailyTemperatures(temperatures))
    # [1,1,4,2,1,1,0,0]
    # [3,1,1,2,1,1,0,1,1,0]
