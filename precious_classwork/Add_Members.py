"""
3. Write a program to convert two lists into a dictionary.
list1(values) = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
list2(key) = [10, 20, 30, 40,  50, 60, 70, 80, 90, 100]
use a loop to iterate through and print the values of the dictionary.
"""

if __name__ == '__main__':

    item_1 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    item_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    dictionary = {item_2[i]: item_1[i]
                  for i in range(10)}
    print(dictionary)





