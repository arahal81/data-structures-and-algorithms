def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)


def merge(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        for item in right[j:]:
            arr[k] = item
            k += 1
    else:
        for item in left[i:]:
            arr[k] = item
            k += 1


# number_list = [20, 18, 12, 8, 5, -2]
# merge_sort(number_list)
# print(number_list)
