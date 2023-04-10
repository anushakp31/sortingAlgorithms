from random import randint
from timeit import repeat


def quicksort(array):

    if len(array) < 2:
        return array

    low, same, high = [], [], []


    pivot = array[randint(0, len(array) - 1)]

    for item in array:

        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)
def run_sorting_algorithm(algorithm, array):

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"


    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)


    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
ARRAY_LENGTH = 100000
if __name__ == "__main__":

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="quicksort", array=array)