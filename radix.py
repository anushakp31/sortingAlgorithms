from random import randint
from timeit import repeat


def countingSortForRadix(inputArray, placeValue):

    countArray = [0] * 10
    inputSize = len(inputArray)


    for i in range(inputSize):
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]


    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]

def radixSort(array):

    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
def run_sorting_algorithm(algorithm, array):

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"


    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
ARRAY_LENGTH = 10000
if __name__ == "__main__":

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="radixSort", array=array)

