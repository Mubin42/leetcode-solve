"""
Problem Name    - Find A String - Python
Link            - https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
Status          - Unsolved
"""


def count_substring(string, sub_string):
    i = 0
    tot = 0
    while i < len(string):
        temp = string[i:len(sub_string) + i]
        if temp == sub_string:
            tot += 1

        i += 1

    return tot


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = "ABCDCDC"
    sub_string = "CDC"
    count = count_substring(string, sub_string)
    print(count)
