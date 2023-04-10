
from random import randint
from timeit import repeat

def insertion_sort(array):

    for i in range(1, len(array)):

        key_item = array[i]


        j = i - 1


        while j >= 0 and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1


        array[j + 1] = key_item

    return array
def run_sorting_algorithm(algorithm, array):

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"


    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
ARRAY_LENGTH = 1000
if __name__ == "__main__":

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]


    run_sorting_algorithm(algorithm="insertion_sort", array=array)