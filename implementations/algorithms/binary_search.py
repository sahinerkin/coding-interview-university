import random

def binary_search(arr: list[int], target: int) -> int:
    l, r = 0, len(arr)
    while l <= r:
        mid = (l + r) // 2
        # print("Mid", mid)

        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1

def binary_search_rec(arr: list[int], target: int, l: int, r: int) -> int:
    mid = (l + r) // 2
    # print("Mid", mid)

    if l > r:
        return -1

    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return binary_search_rec(arr, target, l, mid-1)
    else:
        return binary_search_rec(arr, target, mid+1, r)
    

# All elements unique, to make sure index == found_index when testing
def create_random_sorted_list(size, min_val=1, max_val=100):
    return sorted(random.sample(range(min_val, max_val + 1), size))

if __name__ == "__main__":
    my_list = create_random_sorted_list(50)
    index = 12
    print("List:", my_list)
    print("Looking for element at index", index, "which is", my_list[index])
    
    print("-" * 20)
    print("Iterative binary search")

    found_index = binary_search(my_list, my_list[index])
    print("Found at", found_index)
    
    print("-" * 20)
    print("Recursive binary search")
    found_index = binary_search_rec(my_list, my_list[index], 0, len(my_list)-1)
    print("Found at", found_index)