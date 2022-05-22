# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Input Format
# The first line contains the integer , the number of students' records. The next  lines contain the names and marks
# obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output 0
# 56.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    denominator = len(student_marks[query_name])
    mean_score = sum(student_marks[query_name]) / denominator
    print(f'{mean_score:.2f}')
