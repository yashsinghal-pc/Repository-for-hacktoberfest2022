i# Linear Search or Sequential Search Algorithm
# Time Complexity: O(n)
def sequential_search(arr, item):
    pos = 0
    found = False

    steps = 0
    while pos < len(arr) and not found:
        steps = steps + 1
        if arr[pos] == item:
            found = True
            print(f"Element found at position: {pos} in {steps} steps")
            break
        else:
            pos+=1
    return found
