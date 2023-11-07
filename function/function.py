#!/bin/python3


def bubble_sort(arr):
    for i in range(len(arr)-1):
        print("I loop" + str(i))
        for j in range(i, len(arr)-1):
            print("J loop" + str(j))
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                print(arr)

arr = [1, 2, 5, 6, 3, 7, 4]
bubble_sort(arr)
            
