"""
Mutations Problem - Python (String)
Link: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
Status: Solved
"""


def mutate_string(string: str, position: int, character: str) -> str:
    new_string = ""
    count = 0
    for item in string:
        if count == position:
            new_string += character

        else:
            new_string += item

        count += 1

    return new_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    # s = "abracadabra"
    # i, c = 5, "k"
    s_new = mutate_string(s, int(i), c)
    print(s_new)
