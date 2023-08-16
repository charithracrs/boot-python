# Bubble sorting
# Time Complexity: O(N^2)


# Bubble sort with for loop
def bubble_sort_with_for(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for i in range(n-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] =  data[i+1], data[i]
                swapped = True
        if not swapped:
            break

# Bubble sort with while loop
def bubble_sort_with_while(data):
    sort = False
    n = len(data)
    while not sort:
        swapped = False
        for i in range(n-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] =  data[i+1], data[i]
                swapped = True
        if not swapped:
            sort = True


if __name__ == '__main__':

    data_for = [17, 32, 23, 38, 12]
    bubble_sort_with_for(data_for)
    print(data_for)

    data_while = [13, 43, 27, 36, 9]
    bubble_sort_with_while(data_while)
    print(data_while)