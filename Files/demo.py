# import pathlib
#
# path1 = pathlib.Path("C:\images\ whatsapp\hello.txt")
# path2 = pathlib.Path.cwd()
# path3 = path2 / "private.jpg"
#
# print(path1.is_absolute())
# print(path2)
# print(path3)


def compress_string(values):
    characters = []
    for value in values:
        if value not in values:
            value.append(value)
    for i in range(len(values)):
        if values > i:
            print(values)







