def perms(arr):
    if not arr:
        return [[]]
    result = []
    
    # Pick each element as the first element
    for i in range(len(arr)):
        
        # Remaining elements after removing arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in perms(rest):
            result.append([arr[i]] + p)
            
    return result
def tsp_bruteforce(distance):
    n = len(distance)
    if n == 0:
        return 0, []

    best_cost = float('inf')
    best_path = None

    # Create array for remaining cities: [1, 2, ..., n-1]
    arr = list(range(1, n))

    for order in perms(arr):
        path = [0] + order + [0]  # start at 0, end at 0
        cost = 0
        valid = True

        # total cost of this path
        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            d = distance[a][b]

            if d is None:  # invalid path
                valid = False
                break
            cost += d
            
        if valid and cost < best_cost:
            best_cost = cost
            best_path = path

    return best_cost, best_path
