#2. Search for String "the" and Return Indices
def find_string_indices(text, search_str):
    indices = []
    start = 0
    while True:
        index = text.find(search_str, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices

# Test
text = "The cat and the dog went to the park."
search_str = "the"
indices = find_string_indices(text.lower(), search_str.lower())
print(f"String '{search_str}' found at indices: {indices}")