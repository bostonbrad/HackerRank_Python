# Original challenge can be found here:
# https://www.hackerrank.com/challenges/finding-the-percentage/

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student_average = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        student_average[name] = sum(scores) / len(scores)
    query_name = input()
    average = student_average[query_name]
    format_average = "{:.2f}".format(average)
    print(format_average)
