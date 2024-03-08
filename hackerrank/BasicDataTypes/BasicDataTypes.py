"""
Basic Data Types - Python (List)
Link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
Status: Solved
"""


def parse(items: list) -> None:
    for item in items:
        temp = item.split()
        key = temp[0]
        match key:
            case "insert":
                result.insert(int(temp[1]), int(temp[2]))
            case "print":
                print(result)
            case "remove":
                result.remove(int(temp[1]))
            case "append":
                result.append(int(temp[1]))
            case "sort":
                result.sort()
            case "pop":
                result.pop()
            case "reverse":
                result.reverse()


if __name__ == '__main__':
    # N = int(input("enter: "))
    N = """12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print"""

    result = []
    items = N.split("\n")
    limit = int(items[0])
    del items[0]

    parse(items)
