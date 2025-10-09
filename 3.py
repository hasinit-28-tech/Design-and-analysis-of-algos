#3. CSV Student Data Search
import csv

def search_student_names(csv_file, pattern):
    results = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row_idx, row in enumerate(reader):
                for col_idx, cell in enumerate(row):
                    if pattern.lower() in cell.lower():
                        results.append((row_idx, col_idx, cell))
        return results
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
        return []


with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', '20', 'A'])
    writer.writerow(['Brian', '21', 'B'])
    writer.writerow(['Catherine', '22', 'A'])
    writer.writerow(['David', '19', 'C'])


results = search_student_names('students.csv', 'ai')
print("Names containing 'ai':")
for row, col, name in results:
    print(f"Cell ({row}, {col}): {name}")