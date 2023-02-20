if __name__ == '__main__':
    def palindrome():
        value = input("Input a word: ")
        print()
        value2 = value[::-1]
        if value == value2:
            print(value, "is a palindrome")
    
        else:
            print("This is not a palindrome")


    palindrome()
