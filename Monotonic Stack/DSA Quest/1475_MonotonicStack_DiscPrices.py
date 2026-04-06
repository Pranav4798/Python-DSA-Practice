prices = [8,4,6,2,3]

def finalPrices(prices):
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            last_index = stack.pop()
            prices[last_index] -= prices[i]
        
        stack.append(i)
        
    return prices

print(finalPrices(prices))