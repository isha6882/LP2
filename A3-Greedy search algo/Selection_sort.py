def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]


arr = input('Enter the list of numbers: ').split()
arr = [int(x) for x in arr]
selection_sort(arr)
print('Sorted list: ', end='')
print(arr)


"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""