#1. Text Document Reader with Exception Handling
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print("-" * 30)
            print(content)
            print("-" * 30)
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return ""

# Test
with open('sample.txt', 'w') as f:
    f.write("This is a sample text file.\nIt contains some text for testing.")
read_text_file('sample.txt')
