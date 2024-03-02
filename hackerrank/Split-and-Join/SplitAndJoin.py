def split_and_join(line):
    # write your code here
    line = line.strip()
    a = line.replace(" ", "-")
    return a


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
