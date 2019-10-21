#!/bin/python3

def is_palindrome(test_str):
    """Checks a str for palindrome characteristic"""
    start_i = 0  # Start at beginning of string
    end_j = len(test_str) - 1  # end of string given 0 indexing

    while start_i < end_j:
        if test_str[start_i] == test_str[end_j]:
            start_i += 1
            end_j -= 1
        else:
            print("{} is not a palindrome :(".format(test_str))
            return False
    print("{} is a palindrome :)".format(test_str))
    return True


def recursive_is_palindrome(test_str):
    """Recursive check for str palindrome check"""
    if len(test_str) <= 1:
        print("{} is a palindrome :)".format(test_str))
        return True
    elif test_str[0] == test_str[len(test_str) - 1]:
        return recursive_is_palindrome(test_str[1:-1])
    else:
        print("{} is not a palindrome :(".format(test_str))
        return False


is_palindrome("racecar")
is_palindrome("Vlad")
recursive_is_palindrome("racecar")
recursive_is_palindrome("Vlad")
