"""
Set .add() - Python (Sets)
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Status: Solved
"""

if __name__ == '__main__':
    n = int(input().rstrip())
    countries = []

    for i in range(0, n):
        country = input().strip()
        countries.append(country)

    countries_set = set(countries)

    print(len(countries_set))
