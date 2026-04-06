heights = [2,1,5,6,2,3]

def LargestRectangleArea(heights):
    max_area = 0
    stack = []

    heights.append(0)

    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] >= h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index

        stack.append((start, h))

    heights.pop()
    return max_area


print(LargestRectangleArea(heights))