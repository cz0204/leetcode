#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.


def converting_list_to_number(l):
    number = 0
    for i in range(len(l)):
        digit = l[i]
        number += digit * 10 ** (i)
    return number


def convert_number_to_list(number):
    l = list()
    while number > 0:
        digit = number % 10
        l.append(digit)
        number = (number - digit) // 10
    return l


def adding_two_lists(l_1, l_2):
    number_1 = converting_list_to_number(l_1)
    number_2 = converting_list_to_number(l_2)
    number = number_1 + number_2
    l = convert_number_to_list(number)
    return l


l_1 = [9,9,9,9,9,9,9]
l_2 = [9,9,9,9]

print(adding_two_lists(l_1, l_2))

