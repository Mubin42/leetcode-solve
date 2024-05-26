"""
Grading Students
Link: https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
Status: Solved
"""
from typing import List
import math


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades: List[int]) -> List[int]:
    new_grade = []
    for grade in grades:
        if grade < 38:
            new_grade.append(grade)

        elif grade % 5 > 2:
            i = math.ceil(grade / 5) * 5
            new_grade.append(i)

        else:
            new_grade.append(grade)

    return new_grade


if __name__ == '__main__':
    sample_data = [73, 67, 38, 33]

    result = gradingStudents(sample_data)
    print(result)
