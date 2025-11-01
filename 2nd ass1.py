def get_permutations(items):
    "Return all possible permutations of a given list."
    result = []             
    n = len(items)             

    def helper(current, used):
        # Base case
        if len(current) == n:
            result.append(current.copy())
            return
        for i in range(n):
            if not used[i]:
                used[i] = True             
                current.append(items[i])    
                helper(current, used)       
                current.pop()               
                used[i] = False             

    
    helper([], [False]*n)
    return result


# Example 
numbers = [1, 2, 3]
print("All possible orderings of", numbers, ":")
for order in get_permutations(numbers):
    print(order)
