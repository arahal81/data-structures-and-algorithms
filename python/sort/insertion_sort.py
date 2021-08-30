def insertion_Sort(unsorted_list: list) -> list:
    for i in range(1, len(unsorted_list)):
        j = i - 1
        temp = unsorted_list[i]

        while j >= 0 and temp < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            j = j - 1
            unsorted_list[j] = temp

    return unsorted_list


if __name__ == "__main__":
    print(insertion_Sort([8, 4, 23, 42, 16, 15]))
