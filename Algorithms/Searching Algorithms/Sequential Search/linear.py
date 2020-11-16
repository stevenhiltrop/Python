def lin_search(our_list, key):
    for index in range(0, len(our_list)):
        if our_list[index] == key:
            return index
    else:
        return "not found"


our_list = [15, 1, 9, 3]

print(f"Our list: {our_list}")
print(f"Index of 23 is {lin_search(our_list, 23)}")
print(f"Index of 9 is {lin_search(our_list, 9)}")
