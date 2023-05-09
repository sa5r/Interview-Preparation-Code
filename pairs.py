# takes O(nlgn + lgn)
def pairs_slower(k, arr):
    # python's sort takes O(nlogn)
    arr.sort()

    def binary_search(lst, item):
        mid = int(len(lst) / 2)
        if item == lst[mid]:
            return True
        elif item != lst[mid] and len(lst) == 1:
            return False
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


def pairs(k, arr):
    dict = {}
    counter = 0
    for item in arr:
        dict[item] = 1
        if (item + k) in dict :
            counter += 1
            dict[(item + k)] = 1
        elif (item - k) in dict :
            counter += 1
            dict[(item - k)] = 1
    
    return counter

print(pairs(2, [1,5,3,4,2]))