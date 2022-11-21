def pairs(k, arr):
    # python's sort takes O(nlogn)
    arr.sort()

    def binary_search(lst, item):
        if len(lst) == 1 and lst[0] == item:
            return True
        elif len(lst) == 1 and lst[0] != item:
            return False

        mid = int(len(lst) / 2)
        if item == lst[mid]:
            return True
        elif item < lst[mid]:
            return binary_search(lst[:mid], item)
        elif item > lst[mid]:
            return binary_search(lst[mid:], item)


    counter = 0
    
    for i in range(len(arr)):
        if binary_search(arr, (arr[i] + k)):
            counter += 1
        if (arr[i] + k) > arr[-1]:
            break
    
    return counter

print(pairs(2, [1,2,3,4,5]))