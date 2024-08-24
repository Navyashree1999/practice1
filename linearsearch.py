def binary_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return -1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 15
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")