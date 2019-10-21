#!/bin/python3

def binary_search(find, search):
    left = 0
    right = len(search) - 1

    while left <= right:
        mid = left + (right - left) // 2
        current = search[mid]
        if find == current:
            return mid
        elif find > current:
            left = mid
        else:
            right = mid
    return None


test = [8, 9, 27, 30, 89]
find = 30

assert binary_search(find=30, search=test) == 3 # Should pass 
assert binary_search(find=8, search=test) == 0  # Should pass

try:
    assert binary_search(find=8, search=test) == 1  # Should fail
except AssertionError as e:
    print("Assertion failed correctly")

print("Found {} at index {} in {}".format(find, binary_search(find=find, search=test), test))
