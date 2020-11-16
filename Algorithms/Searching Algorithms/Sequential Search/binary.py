def binary_search(our_list, key):
    left = 0 # I assign left position to zero
    right = len(our_list) - 1 # I assign right position by defining the length of ourlist minus one
    matched = False
    while left <= right and not matched: # the loop will continue untill the left element is less or equal to the right element and the matched is True
        mid = (left+right)//2 # I find the position of the middle element
        if our_list[mid] == key: # if the middle element corresponds to the key element
            matched = True
        else:  # otherwise
            if key < our_list[mid]: # if key element is less than the middle element
                right = mid - 1 # I assign the position of the right element as mid - 1
            else: # otherwise
                left = mid + 1 # left position will become the middle position plus 1
    return matched


our_list = [1, 3, 9, 15]
print(f"Our list: {our_list}")
print(f"17 in our list? {binary_search(our_list, 17)}")
print(f"3 in our list? {binary_search(our_list, 3)}")
