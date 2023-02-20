if __name__ == '__main__':
    my_str = 'This is a test'
    string_elements = my_str.split()
    print(string_elements)
    # ['This','is','a','test']
    reversed_elements = []
    for element in string_elements:
        reversed_elements.append(element[::-1])

    print(reversed_elements)
    # ['sihT','si','a','tset']
    # new_str = ' '.join(reversed_elements)
    # print(new_str)
    # 'sihT si a tset'
