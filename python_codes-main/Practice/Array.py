import array

def printArr(i, arr):

    if(i < len(arr)):
        print(arr[i], end = " ")
        printArr(i + 1, arr)

arr = array.array('i', [10, 20, 30, 40, 50])
printArr(0, arr)
