#implement Permutation from scratch (do not use inbuilt methods) - For any data type using the daa concepts
# PERMUTATION 

def generate_permutations(arr):
    result = []
    # Backtracking function
    def permute(current_index):
        # If we fixed all positions → store the permutation
        if current_index == len(arr):
            result.append(arr.copy())
            return

        # Try placing each element at the current index
        for i in range(current_index, len(arr)):
            arr[current_index], arr[i] = arr[i], arr[current_index]
            permute(current_index + 1)
            arr[current_index], arr[i] = arr[i], arr[current_index]

    permute(0)
    return result
#example:
data = [1, "A", 3]     
perms = generate_permutations(data)

print("All permutations:")
for p in perms:
    print(p)

