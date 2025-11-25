def generate_combinations(arr, k):
    "Generate all combinations of length k from arr."
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()  
    backtrack(0, [])
    return result
def knapsack_bruteforce_combinations(values, weights, capacity):
    n = len(values)
    best_value = 0
    best_items = []
    for k in range(n + 1):
        for combo in generate_combinations(list(range(n)), k):
            total_weight = sum(weights[i] for i in combo)
            total_value = sum(values[i] for i in combo)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_items = combo.copy()
    return best_value, best_items
# Example 
values = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
capacity = 15

best_value, best_items = knapsack_bruteforce_combinations(values, weights, capacity)

print("Best total value:", best_value)
print("Items chosen:")
for i in best_items:
    print(f"  Item {i}: Value = {values[i]}, Weight = {weights[i]}")

