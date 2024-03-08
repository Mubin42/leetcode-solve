"""
Problem Name    - Finding The Percentage - Python (String)
Link            - https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
Status          - Solved
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    score = student_marks[query_name]
    total = 0
    for item in score:
        total += item

    result = (total/len(score))
    result = "{:.2f}".format(result)
    print(result)


