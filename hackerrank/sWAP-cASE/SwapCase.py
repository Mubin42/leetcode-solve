"""
Swap Case Problem - Python
Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
Status: Solved
"""


def swap_case(s: str) -> str:
    new_string = ""
    for character in s:
        if character.isupper():
            new_string += character.lower()

        elif character.islower():
            new_string += character.upper()

        else:
            new_string += character

    return new_string


if __name__ == '__main__':
    # s = input()
    s = "Www.HackerRank.com"
    result = swap_case(s)
    print(result)
