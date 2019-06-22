# quick sort code
from random import randint
import time

comparisons = 0

def main():
    start = time.time()

    text = open(r'E:\Summer 2019\Algorithms\Quick Sort\QuickSort.txt')
    content = text.read().splitlines()
    num = []

    for line in content:
        num.append(int(line))
    text.close

    quickSort(num)

    sort = open(r'E:\Summer 2019\Algorithms\Quick Sort\pset2_qn1_solution.txt', 'w')

    for item in num:
        sort.write(f'{str(item)}\n')
    sort.close()

    print(comparisons)
    print("--- %s seconds ---" % (time.time() - start))

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


def quickSortHelper(arr, leftIndex, rightIndex):
    global comparisons 

    if leftIndex < rightIndex:

        comparisons += rightIndex - leftIndex
        pivot = partition(arr, leftIndex, rightIndex)

        quickSortHelper(arr, leftIndex, pivot - 1)
        quickSortHelper(arr, pivot + 1, rightIndex)


def partition(arr, leftIndex, rightIndex):

        # randomly generated pivot
        # randIndex = randint(leftIndex, rightIndex)

        # swap if the above line is uncommented
        # arr[leftIndex], arr[randIndex] = arr[randIndex], arr[leftIndex]


        pivot = leftIndex + 1

        # partitioning 
        for index in range(pivot, rightIndex + 1):
            if arr[index] < arr[leftIndex]:

                arr[index], arr[pivot] = arr[pivot], arr[index]
                pivot += 1

        #reswap the pivot
        pivot -= 1
        arr[leftIndex], arr[pivot] = arr[pivot], arr[leftIndex]

        return pivot



if __name__ == "__main__":
    main()