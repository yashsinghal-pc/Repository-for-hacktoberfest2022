#Binary Search using python Iterative method

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1
  mid = 0
  while low <= high:
    mid = (high + low) // 2
    if arr[mid] < target:
      low = mid + 1
    elif arr[mid] > target:
      high = mid - 1
    else:
      return mid
  return -1

arr = [1,2,3,4,5,6 ]
target = 3

result = binary_search(arr, target)
if result != -1:
	print(f"{target} present at index number {result}")
else:
	print(f"{target} is not present in  the array")
