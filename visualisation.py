import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]

def heapify(arr, n, i):
    largest = i
    l = i * 2 + 1
    r = i * 2 + 2
    while l < n and arr[l] > arr[largest]:
        largest = l
    while r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        swap(arr, i, largest)
        yield arr
        yield from heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        yield from heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        yield arr
        yield from heapify(arr, i, 0)
def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        yield from heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        yield arr
        yield from heapify(arr, i, 0)

def bubblesort(A):

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


def insertionSort(A):

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A


def mergesort(A, start, end):

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A


def merge(A, start, mid, end):


    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A


def quicksort(A, start, end):

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


def num_digits(arr):
    maxDigit = 0
    for num in arr:
        maxDigit = max(maxDigit, num)
    return len(str(maxDigit))


# flatten into a 1D List
from functools import reduce


def flatten(arr):
    return reduce(lambda x, y: x + y, arr)


def radix(arr):

    digits = num_digits(arr)
    for digit in range(0, digits):
        temp = [[] for i in range(10)]
        for item in arr:
            num = (item // (10 ** digit)) % 10
            temp[num].append(item)
        arr = flatten(temp)

    return arr


if __name__ == "__main__":

    N = int(input("Enter number of integers: "))
    method_msg = "Enter sorting method:\n(1) Merge Sort\n(2) Heap sort\n(3) Quicksort \
        \n(4) Insertion sort\n(5) Radix sort\n"
    method = input(method_msg)

    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)
    print("Unsorted array: " + str(A))

    if method == "1":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    elif method == "2":
        title = "Heap sort"
        generator = heap_sort(A)
    elif method == "3":
        title = "Quicksort"
        generator = quicksort(A, 0, N - 1)
    elif method == "4":
        title = "Insertion sort"
        generator = insertionSort(A)
    elif method=="5":

        c=[]
        c=radix(A)
        print("Sorted array :" + str(c))

        exit()
    else :
        print("Invalid option")
        exit()


    start = time.time()
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(A)), A, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    text1 = ax.text(0.01, 0.90, "", transform=ax.transAxes)

    iteration = [0]


    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        endtime = time.time()

        text.set_text("# of operations: {}".format(iteration[0]))
        timing = endtime - start
        text1.set_text("Time : {}" .format(timing))


    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=generator, interval=1,
                                   repeat=False)

    plt.show()
