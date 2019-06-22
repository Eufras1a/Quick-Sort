from random import randint

comparisons = 0

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


def quickSortHelper(arr, leftIndex, rightIndex):
    global comparisons

    if leftIndex < rightIndex:
        comparisons += rightIndex - leftIndex
        print(comparisons, rightIndex, leftIndex, arr)
        pivot = partition(arr, leftIndex, rightIndex)

        quickSortHelper(arr, leftIndex, pivot - 1)
        quickSortHelper(arr, pivot + 1, rightIndex)


def partition(arr, leftIndex, rightIndex):

# -------------------------------------- random pivot method ------------------------------------------------------------------------
       # randPivot(arr, leftIndex, rightIndex)

# -------------------------------------- last element pivot method -------------------------------------------------------------------
       # rightPivot(arr, leftIndex, rightIndex)

# -------------------------------------- median of three pivot method ----------------------------------------------------------------
       # medianPivot(arr, leftIndex, rightIndex)


# -------------------------------------- first element pivot method if none of the above are uncommented -----------------------------


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

def rightPivot(arr, leftIndex, rightIndex):
    # swapping the first and the last element 
    arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]
    
def randPivot(arr, leftIndex, rightIndex):
    # randomly generated pivot
    randIndex = randint(leftIndex, rightIndex)

    # swap if the above line is uncommented
    arr[leftIndex], arr[randIndex] = arr[randIndex], arr[leftIndex]

def medianPivot(arr, leftIndex, rightIndex):
    mid = arr[((rightIndex - leftIndex) // 2) + leftIndex]
    median = [arr[leftIndex], mid, arr[rightIndex]]
    median = sorted(median)

    return median[1]

if __name__ == "__main__":
    A = [3, 8, 2, 5, 1, 4, 4]

#     quickSort(A)
#     print(A)
#     print(comparisons)

    medianPivot(A, 0, len(A) - 1)