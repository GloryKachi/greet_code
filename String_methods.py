if __name__ == '__main__':
    s = "Hello world"
    print(s.upper())
    print(s.lower())
    print(s.capitalize())
    print(s.title())

    for i in range(1, 20, 2):
        s = '*' * i
        print(s.center(20))
        binary = '0011101000111010100100'
        print(binary.translate(str.maketrans('01', '10')))

import string
word = input("Enter a word: ")
key = int(input("Enter the key to code with: "))
abc = string.ascii_lowercase
inverse = abc[key:] + abc[:key]
print(word.translate(str.maketrans(inverse,abc)))