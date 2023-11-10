############ Programmer -> Owolabi Badmus ############
############ Date -> 11/10/2023 ############

# Binary Search Algorithm
def binary_search(num: int, arr: list) -> dict:
    if not num in arr:
        return "Number does not exists."

    arr.sort()
    iteration = 0
    
    while True:

        iteration += 1
        mid_index = len(arr) // 2
        mid_num = arr[mid_index]

        if num == mid_num:
            return {"num": num, "index": mid_index, "iteration": iteration, "arr": arr}
        if num > mid_num:
            arr = arr[mid_index+1:]
        elif num < mid_num:
            arr = arr[:mid_index]

# Test
array = [15, 28, 36, 44, 53, 62, 71, 88, 106, 20]
print(binary_search(16, array))