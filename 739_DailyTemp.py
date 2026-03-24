temperatures = [73,74,75,71,69,72,76,73]

def DailyT(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stack_t, stack_ind = stack.pop()

            res[stack_ind] = i - stack_ind

        stack.append([t, i])

    return res

print(DailyT(temperatures))