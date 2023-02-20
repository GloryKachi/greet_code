string1 = "aabcccdddddd"


def compress_string(string):
    unique_value = []
    for char in string:
        if char not in unique_value:
            unique_value.append(char)

    for char in unique_value:
        count = 0
        for i in range(len(string)):
            if string[i] == char:
                count += 1
        print(char, count, end="", sep="")


if __name__ == '__main__':
    compress_string(string1)
