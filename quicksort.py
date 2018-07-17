# Quicksort in action


def quicksort(array):
    # Lets take care of our base case
    # arrays with 0 or 1 element are already sorted!
    if len(array) < 2:
        return array
    else:
        # Set our pivot
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  # Create an array of all element less than pivot

        greater = [i for i in array[1:] if i > pivot]  # Create an array of all elements greater than pivot

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([200, 5, 10, -400]))
