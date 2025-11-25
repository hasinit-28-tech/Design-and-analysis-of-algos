#mplement combination from scratch (do not use inbuilt methods) - For any data type using the daa concepts
# COMBINATIONS (WORKS FOR ANY DATA TYPE)

def generate_combinations(arr, k):
    result = []
    current = []

    def backtrack(start):
        if len(current) == k:
            result.append(current.copy())
            return
        for i in range(start, len(arr)):
            current.append(arr[i])   # choose
            backtrack(i + 1)        # recurse
            current.pop()           # un-choose (backtrack)

    backtrack(0)
    return result

# Example Usage
data = ["A", 2, "X", 5]   # any data type
k = 2
combs = generate_combinations(data, k)
print("All combinations:")
for c in combs:
    print(c)
