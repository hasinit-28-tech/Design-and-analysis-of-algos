
def perms(lst):
    if not lst:
        return [[]]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in perms(rest):
            result.append([lst[i]] + p)
    return result

def tsp_bruteforce(distance):
    
    n = len(distance)
    if n == 0:
        return 0, []

    best_cost = float('inf')
    best_path = None

    rest_cities = list(range(1, n))

    for order in perms(rest_cities):
        path = [0] + order + [0]  
        cost = 0
        valid = True
        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            d = distance[a][b]
            if d is None:
                valid = False
                break
            cost += d
        if valid and cost < best_cost:
            best_cost = cost
            best_path = path

    return best_cost, best_path


# Example 
dist = [
    [0, 2, 9, 10, 7],
    [1, 0, 6, 4, 3],
    [15,7, 0, 8, 9],
    [6, 3, 12,0, 11],
    [10,4,8, 5, 0]
]

cost, path = tsp_bruteforce(dist)
print("Best route cost:", cost)
print("Best route (visit order):", path)
