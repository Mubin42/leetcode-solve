import textwrap


def wrap(string, max_width):
    count = 0
    wrap_str = ""
    for char in string:
        if count > max_width - 1:
            wrap_str += "\n"
            count = 0
        wrap_str += char
        count += 1

    return wrap_str


if __name__ == '__main__':
    string, max_width = input(), int(input())
    # string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    result = wrap(string, max_width)
    print(result)
